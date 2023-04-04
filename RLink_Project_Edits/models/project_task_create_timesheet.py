from odoo import api, models, fields, _
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, ValidationError


class ProjectTaskCreateTimesheet_inherited(models.TransientModel):
    _inherit = 'project.task.create.timesheet'

    # @api.constrains('description')
    # def _check_description_len(self):
    #     for rec in self:
    #         if not rec.description or len(rec.description) < 25:
    #             raise ValidationError("Description should be more than 25 character")

    def save_timesheet(self):
        if not self.description or len(self.description) < 25:
           raise ValidationError("Description should be more than 25 character")
        values = {

            'task_id': self.task_id.id,
            'project_id': self.task_id.project_id.id,
            'date': fields.Date.context_today(self),
            'name': self.description,
            'user_id': self.env.uid,
            'unit_amount': self.time_spent,
        }
        self.task_id.user_timer_id.unlink()
        return self.env['account.analytic.line'].create(values)
