from odoo import api, models, fields, _

from odoo.exceptions import UserError, ValidationError


class ProjectInherited(models.Model):
    _inherit = 'project.project'

    @api.model
    def create(self, vals):
        rec = super(ProjectInherited, self).create(vals)
        to_do = self.env['project.task.type'].search([('name', '=', 'To Do')], limit=1)
        doing = self.env['project.task.type'].search([('name', '=', 'Doing')], limit=1)
        to_check = self.env['project.task.type'].search([('name', '=', 'To Check')], limit=1)
        done = self.env['project.task.type'].search([('name', '=', 'Done')], limit=1)
        if not to_do:
            to_do = self.env['project.task.type'].create({'name': 'To Do', 'sequence': 1})
        if not doing:
            doing = self.env['project.task.type'].create({'name': 'Doing', 'sequence': 2})
        if not to_check:
            to_check = self.env['project.task.type'].create({'name': 'To Check', 'sequence': 3})
        if not done:
            done = self.env['project.task.type'].create({'name': 'Done', 'sequence': 4})
        type_ids = [to_do.id, doing.id, to_check.id, done.id]
        rec.type_ids = type_ids
        return rec


class ProjectTaskInherited(models.Model):
    _inherit = 'project.task'

    speed = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'),
                              ('4', '4'), ('5', '5')], string='Speed')
    quality = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'),
                                ('4', '4'), ('5', '5')], string='Quality')
    no_repeated_errors = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'),
                                           ('4', '4'), ('5', '5')], string='No Repeated Error')
    requested_by = fields.Many2many('res.users', readonly=True, related='user_ids', string="Requested By")
    # description = fields.Html(required=True)

    # @api.constrains('description')
    # def _check_len_html(self):
    #     print(self.description, len(self.description))
    #     if len(self.description) < 25 + 7:
    #         raise ValidationError("Description should be more than 25 character")
