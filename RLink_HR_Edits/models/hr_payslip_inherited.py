from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError, Warning


class HrPayslipInherited(models.Model):
    _inherit = 'hr.payslip'

    exchange_rate = fields.Monetary('Exchange Rate', required=1)

  

