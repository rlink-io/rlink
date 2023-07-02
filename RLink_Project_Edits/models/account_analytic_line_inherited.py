from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError


class AccountAnalyticLineInherited(models.Model):
    _inherit = 'account.analytic.line'

    document_attachment = fields.Binary(string="Document")

    @api.constrains('name')
    def _check_timesheet_name_len(self):
        for rec in self:
            print(rec.name, rec.document_attachment)
            if rec.project_id and rec.task_id:
                if len(rec.name) < 25:
                    raise ValidationError(
                        "The Description of timesheet  cannot be empty and should be more than 25 characters.")
