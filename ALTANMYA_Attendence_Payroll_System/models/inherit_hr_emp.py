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
    deduction_ids = fields.One2many('hr.deduction', 'employee_id')
    violation_ids = fields.One2many('hr.violation', 'employee_id')
    training_id = fields.Many2one('hr.training')
    days_off_id = fields.Many2one('hr.days.off')

    def call_deduction_action(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("ALTANMYA_Attendence_Payroll_System.hr_deduction_action")
        action['context'] = dict(self._context, default_employee_id=self.id, )
        action['domain'] = [('employee_id', '=', self.id)]
        return action

    def call_violation_action(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("ALTANMYA_Attendence_Payroll_System.hr_violation_action")
        action['context'] = dict(self._context, default_employee_id=self.id, )
        action['domain'] = [('employee_id', '=', self.id)]
        return action

    def call_training_action(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("ALTANMYA_Attendence_Payroll_System.hr_training_action")
        action['context'] = dict(self._context, default_employee_id=self.id, )
        if self.training_id:
            action['res_id'] = self.training_id.id
        return action

    def call_days_off_action(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("ALTANMYA_Attendence_Payroll_System.hr_days_off_action")
        action['context'] = dict(self._context, default_employee_id=self.id, )
        if self.days_off_id:
            action['res_id'] = self.days_off_id.id
        return action


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
