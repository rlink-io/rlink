from odoo import api, models, fields, _
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, ValidationError


class ProjectTaskCreateTimesheet_inherited(models.TransientModel):
    _inherit = 'project.task.create.timesheet'

    @api.constrains('description')
    def _check_description_len(self):
        for rec in self:
            if not rec.description or len(rec.description) < 25:
                raise ValidationError("Description should be more than 25 character")
