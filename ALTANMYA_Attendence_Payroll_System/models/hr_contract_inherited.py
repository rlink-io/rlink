from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError


class HrContractInherited(models.Model):
    _inherit = 'hr.contract'

    probation_period_start_date = fields.Date(string='Probation Period Start Date')
    permanent_period_start_date = fields.Date(string='Permanent Period Start Date')
    probation_period_salary = fields.Monetary(string='Probation Period Salary')
    permanent_period_salary = fields.Monetary(string='Permanent Period Salary')
    leave_date = fields.Date(string='Leave Date')
    leave_reason = fields.Char(string='Reason')

    def write(self, values):
        if 'probation_period_salary' in values and values['probation_period_salary'] < 0:
            raise ValidationError('You can\'t enter negative value for Probation Period Salary')
        elif 'permanent_period_salary' in values and values['permanent_period_salary'] < 0:
            raise ValidationError('You can\'t enter negative value for Permanent Period Salary')
        else:
            return super(HrContractInherited, self).write(values)

    @api.model
    def create(self, vals_list):
        if 'probation_period_salary' in vals_list and vals_list['probation_period_salary'] < 0:
            raise ValidationError('You can\'t enter negative value for Probation Period Salary')
        elif 'permanent_period_salary' in vals_list and vals_list['permanent_period_salary'] < 0:
            raise ValidationError('You can\'t enter negative value for Permanent Period Salary')
        else:
            return super(HrContractInherited, self).create(vals_list)


class HrContractHistoryInherited(models.Model):
    _inherit = 'hr.contract.history'
    advanced_payment_ids = fields.One2many('hr.advanced.payment', 'contract_history_id')

    def call_advanced_payment_action(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id(
            "ALTANMYA_Attendence_Payroll_System.hr_advanced_payment_action")
        action['context'] = dict(self._context, default_contract_history_id=self.id, )
        action['domain'] = [('contract_history_id', '=', self.id)]
        return action


class AdvancedPayment(models.Model):
    _name = 'hr.advanced.payment'
    _description = "Employee Advanced Payment"

    date = fields.Date(string="Payment Date")
    value = fields.Monetary(string="Payment Value")
    employee_id = fields.Many2one('hr.employee', related='contract_history_id.employee_id')
    contract_history_id = fields.Many2one('hr.contract.history', required=True)
    company_id = fields.Many2one('res.company', related='employee_id.company_id', readonly=False,
                                 default=lambda self: self.env.company, required=True)
    currency_id = fields.Many2one(string="Currency", related='company_id.currency_id', readonly=True)

    def write(self, vals):
        if 'value' in vals and vals['value'] < 0:
            raise ValidationError('You can\'t enter negative value for Advanced Payment Value')
        else:
            return super(AdvancedPayment, self).write(vals)

    @api.model
    def create(self, vals_list):
        print(vals_list)
        if 'value' in vals_list and vals_list['value'] < 0:
            raise ValidationError('You can\'t enter negative value for Advanced Payment Value')
        else:
            return super(AdvancedPayment, self).create(vals_list)
