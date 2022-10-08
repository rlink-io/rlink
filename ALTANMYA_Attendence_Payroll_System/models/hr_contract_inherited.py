from odoo import api, models, fields


class HrContractInherited(models.Model):
    _inherit = 'hr.contract'

    probation_period_start_date = fields.Date(string='Probation Period Start Date')
    permanent_period_start_date = fields.Date(string='Permanent Period Start Date')
    probation_period_salary = fields.Monetary(string='Probation Period Salary')
    permanent_period_salary = fields.Monetary(string='Permanent Period Salary')
    leave_date = fields.Date(string='Leave Date')
    leave_reason = fields.Char(string= 'Reason')
