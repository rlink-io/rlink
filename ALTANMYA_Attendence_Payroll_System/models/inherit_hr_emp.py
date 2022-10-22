from odoo import api, models, fields, _


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
    bonus_ids = fields.One2many('hr.bonus', 'employee_id')
    training_ids = fields.One2many('hr.training', 'employee_id')
    days_off_id = fields.Many2one('hr.days.off')
    salary_raise_ids = fields.One2many('hr.salary.raise', 'employee_id')
    assessment_id = fields.Many2one('hr.assessment')
    state = fields.Selection([('confirmation_needed', 'Confirmation Needed'), ('confirmed', 'Confirmed')],
                             default='confirmed')
    change_request = fields.One2many('hr.change.request', 'employee_id')

    @api.model
    def create(self, vals):
        new = super(ExtendEmp, self).create(vals)
        employees = self.env['hr.employee'].search([])
        for employee in employees:
            if not employee.assessment_id:
                assessment = self.env['hr.assessment'].sudo().create({
                    "employee_id": employee.id
                })
        return new

    def write(self, values):
        if 'assessment_id' in values:
            super(ExtendEmp, self).write(values)

        elif not self.env.user.has_group('hr.group_hr_manager') and self.user_id.state != 'new':
            self.create_change_request(values)
            super(ExtendEmp, self).write({'state': 'confirmation_needed'})

        else:
            super(ExtendEmp, self).write(values)

    def create_change_request(self, values):

        previous_value = ''
        for val in values:
            field_name = str(self._fields[val]).split('.')[-1]
            if isinstance(self._fields[val], (fields.Many2one, fields.Many2many, fields.One2many)):
                field_type = 'relation'
                previous_value = self[val].name
                model_name = self._fields[val].comodel_name
                new_value = self.env[model_name].sudo().search([('id', '=', values[val])]).name

            elif isinstance(self._fields[val], fields.Selection) and isinstance(self._fields[field_name].selection,
                                                                                list):
                field_type = 'selection'
                kay_val_dict = dict(self._fields[field_name].selection)
                for key, value in kay_val_dict.items():
                    if key == self[val]:
                        previous_value = value
                    if key == values[val]:
                        new_value = value

            else:
                previous_value = self[val]
                new_value = values[val]
                field_type = 'normal'

            self.env['hr.change.request'].create({
                'employee_id': self.id,
                'field_type': field_type,
                'field_string': self._fields[val].string if self._fields[val].string else self._fields[val],
                'field_name': field_name,
                'previous_value_origin': self[val],
                'previous_value': previous_value,
                'new_value_origin': values[val],
                'new_value': new_value
            })

        return values

    def open_emp_kanban(self):
        form_id = self.env.ref('hr.hr_kanban_view_employees').id
        if self.env.user.has_group('hr.group_hr_manager'):
            action = self.env["ir.actions.actions"]._for_xml_id("hr.open_view_employee_list_my")
            return action
        else:
            return {
                'name': 'My Profile',
                'view_mode': 'kanban',
                'view_type': 'kanban',
                'view_id': form_id,
                'context': {},
                'res_model': 'hr.employee',
                'type': 'ir.actions.act_window',
            }

    def open_emp_profile(self):
        form_id = self.env.ref('hr.view_employee_form').id
        self.env['res.users'].search([('id', '=', self._uid)], limit=1)
        emp = self.env['hr.employee'].search([('user_id', '=', self._uid)])
        print(emp)
        return {
            'name': 'My Profile',
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': form_id,
            'context': {},
            'res_model': 'hr.employee',
            'res_id': emp.id,
            'type': 'ir.actions.act_window',
        }

    #
    # def cmd_send_notification(self):
    #     return {
    #         'type': 'ir.actions.client',
    #         'tag': 'display_notification',
    #         'params': {
    #             'title': _('Your Custom Notification Title'),
    #             'message': 'Your Custom Message...',
    #             'sticky': False,
    #         }
    #     }

    def call_deductions_action(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("ALTANMYA_Attendence_Payroll_System.hr_deduction_action")
        action['context'] = dict(self._context, default_employee_id=self.id, )
        action['domain'] = [('employee_id', '=', self.id)]
        return action

    def call_bonuses_action(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("ALTANMYA_Attendence_Payroll_System.hr_bonus_action")
        action['context'] = dict(self._context, default_employee_id=self.id, )
        action['domain'] = [('employee_id', '=', self.id)]
        return action

    def call_salary_raises_action(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("ALTANMYA_Attendence_Payroll_System.hr_salary_raise_action")
        action['context'] = dict(self._context, default_employee_id=self.id, )
        action['domain'] = [('employee_id', '=', self.id)]
        return action

    def call_violations_action(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("ALTANMYA_Attendence_Payroll_System.hr_violation_action")
        action['context'] = dict(self._context, default_employee_id=self.id, )
        action['domain'] = [('employee_id', '=', self.id)]
        return action

    def call_trainings_action(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("ALTANMYA_Attendence_Payroll_System.hr_training_action")
        action['context'] = dict(self._context, default_employee_id=self.id, )
        action['domain'] = [('employee_id', '=', self.id)]
        return action

    def call_days_off_action(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("ALTANMYA_Attendence_Payroll_System.hr_days_off_action")
        action['context'] = dict(self._context, default_employee_id=self.id, )
        if self.days_off_id:
            action['res_id'] = self.days_off_id.id
        return action

    def call_assessment_action(self):
        self.ensure_one()
        if not self.assessment_id:
            self.env['hr.assessment'].sudo().create({
                "employee_id": self.id
            })
        action = self.env["ir.actions.actions"]._for_xml_id("ALTANMYA_Attendence_Payroll_System.hr_assessment_action")
        action['context'] = dict(self._context, default_employee_id=self.id, )
        action['res_id'] = self.assessment_id.id
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


class EmployeeChangeRequest(models.Model):
    _name = "hr.change.request"
    _description = "Employee Change Request"

    employee_id = fields.Many2one('hr.employee')
    field_string = fields.Char(string='Field Name')
    field_name = fields.Char()
    previous_value = fields.Char(string='Previous Value')
    previous_value_origin = fields.Char()
    new_value = fields.Char(string='New Value')
    new_value_origin = fields.Char()
    field_type = fields.Char()
    status = fields.Selection([('pending', 'Pending'), ('confirmed', 'Confirmed'), ('rejected', 'Rejected')],
                              default='pending')

    def check_emp_state(self):
        to_be_confirmed = self.env['hr.change.request'].sudo().search(
            [('employee_id', '=', self.employee_id.id), ('status', '=', 'pending')])
        if not to_be_confirmed:
            self.employee_id.write({'state': 'confirmed'})

    def confirm_request(self):
        if self.env.user.has_group('hr.group_hr_manager'):
            if self.field_type == 'relation':
                value = int(self.new_value_origin)
            else:
                value = self.new_value_origin
            val = {self.field_name: value}
            self.employee_id.sudo().write(val)
            self.status = 'confirmed'
            self.check_emp_state()

    def reject_request(self):
        if self.env.user.has_group('hr.group_hr_manager'):
            self.status = 'rejected'
            self.check_emp_state()
