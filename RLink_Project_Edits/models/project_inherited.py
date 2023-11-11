from odoo import api, models, fields, _
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError

import logging
_logger = logging.getLogger(__name__)
class ProjectInherited(models.Model):
    _inherit = 'project.project'

    @api.model
    def create(self, vals):
      
           
        rec = super(ProjectInherited, self).create(vals)
        if 'user_id' in vals:
            self.env['res.users'].sudo().browse(rec.user_id.id).write({
                     'groups_id': [(4, self.env.ref('project.group_project_manager').id)]
                })

        to_do = self.env['project.task.type'].create({'name': 'To Do', 'sequence': 1})

        doing = self.env['project.task.type'].create({'name': 'Doing', 'sequence': 2})

        to_check = self.env['project.task.type'].create({'name': 'To Check', 'sequence': 3})

        done = self.env['project.task.type'].create({'name': 'Done', 'sequence': 4})
        type_ids = [to_do.id, doing.id, to_check.id, done.id]
        rec.type_ids = type_ids
        return rec

    def write(self, vals):
        # directly compute is_favorite to dodge allow write access right
        if 'is_favorite' in vals:
            vals.pop('is_favorite')
            self._fields['is_favorite'].determine_inverse(self)
        res = super(ProjectInherited, self).write(vals) if vals else True
        if 'user_id' in vals:
            self.env['res.users'].sudo().browse(vals['user_id']).write({
                     'groups_id': [(4, self.env.ref('project.group_project_manager').id)]
                })

        if 'allow_recurring_tasks' in vals and not vals.get('allow_recurring_tasks'):
            self.env['project.task'].search([('project_id', 'in', self.ids), ('recurring_task', '=', True)]).write({'recurring_task': False})

        if 'active' in vals:
            # archiving/unarchiving a project does it on its tasks, too
            self.with_context(active_test=False).mapped('tasks').write({'active': vals['active']})
        if vals.get('partner_id') or vals.get('privacy_visibility'):
            for project in self.filtered(lambda project: project.privacy_visibility == 'portal'):
                project.message_subscribe(project.partner_id.ids)
        if vals.get('privacy_visibility'):
            self._change_privacy_visibility()
        if 'name' in vals and self.analytic_account_id:
            projects_read_group = self.env['project.project'].read_group(
                [('analytic_account_id', 'in', self.analytic_account_id.ids)],
                ['analytic_account_id'],
                ['analytic_account_id']
            )
            analytic_account_to_update = self.env['account.analytic.account'].browse([
                res['analytic_account_id'][0]
                for res in projects_read_group
                if res['analytic_account_id'] and res['analytic_account_id_count'] == 1
            ])
            analytic_account_to_update.write({'name': self.name})
        return res
