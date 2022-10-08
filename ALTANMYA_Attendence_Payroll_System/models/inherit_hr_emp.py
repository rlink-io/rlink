from odoo import api, models, fields

class ExtendEmp(models.Model):
    _inherit = 'hr.employee'
    # _name = 'attendance.employee'

    studio_employee_number = fields.Integer(string='Id on device')
    att_mode = fields.Selection([('standard', 'Standard mode'), ('daily', 'Daily mode'), ('classic', 'Classic mode'),
                                 ('sequential', 'Sequential mode'), ('shift', 'Shift mode')], string='Attendance Mode',
                                index=True)
    father_name = fields.Char(string='Father\'s Name')
    mother_name = fields.Char(string='Mother\'s Name')
    Landline_number = fields.Char(string='Landline Number')
    military_status = fields.Selection([('served', 'Served'), ('not_served', 'Not Served'),
                                        ('exempted', 'Exempted'), ('not_applicable', 'Not Applicable')])
    insurance_card_number = fields.Char(string='Insurance Card Number')
    bank_account_number = fields.Char(string='Bank Account Number')
    # deduction_history = fields.Many2one('hr.deduction.history', compute='_compute_deduction_history')

    # def action_open_deduction_history(self):
    #     self.ensure_one()
    #     action = self.env["ir.actions.actions"]._for_xml_id("ALTANMYA_Attendence_Payroll_System.hr_deduction_history_action")
    #     action['res_id'] = self.deduction_history.id
    #     return action

    # def _compute_deduction_history(self):
    #     for emp in self:
    #         if not emp.deduction_history:
    #             deduction_history = self.env['hr.deduction.history'].create({'employee_id': emp.id})
    #             emp.deduction_history = deduction_history.id


class ExtendEmpPub(models.Model):
    _inherit = 'hr.employee.public'
    # _name = 'attendance.employee'

    studio_employee_number = fields.Integer(string='Id on device')
    att_mode = fields.Selection([('standard', 'Standard mode'), ('daily', 'Daily mode'), ('classic', 'Classic mode'),
                                 ('sequential', 'Sequential mode'), ('shift', 'Shift mode')], string='Attendance Mode',
                                index=True)
    # att_mode = fields.Selection( string='Attendance Mode',compute='_att_mode')
#
#     def _studio_employee_number(self):
#         for rec in self:
#             rec.studio_employee_number=super('ExtendEmpPub',rec).employee_id.studio_employee_number
#
#     def _att_mode(self):
#         for rec in self:
#             rec.studio_employee_number=super('ExtendEmpPub',rec).employee_id.att_mode
