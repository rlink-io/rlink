from odoo import api, models, fields, _


class AccountAnalyticLineInherited(models.Model):
    _inherit = 'account.analytic.line'

    document_attachment = fields.Binary(string="Document")

