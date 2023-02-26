from odoo import api, models, fields, _
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError


class ProjectInherited(models.Model):
    _inherit = 'project.project'

    @api.model
    def create(self, vals):
        rec = super(ProjectInherited, self).create(vals)

        to_do = self.env['project.task.type'].create({'name': 'To Do', 'sequence': 1})

        doing = self.env['project.task.type'].create({'name': 'Doing', 'sequence': 2})

        to_check = self.env['project.task.type'].create({'name': 'To Check', 'sequence': 3})

        done = self.env['project.task.type'].create({'name': 'Done', 'sequence': 4})
        type_ids = [to_do.id, doing.id, to_check.id, done.id]
        rec.type_ids = type_ids
        return rec
