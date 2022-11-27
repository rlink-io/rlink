from odoo import api, models, fields, _


class EmployeeChangeRequest(models.Model):
    _name = "hr.change.request"
    _description = "Employee Change Request"

    employee_id = fields.Many2one('hr.employee')
    user_id = fields.Many2one(related='employee_id.user_id')
    field_label = fields.Char(string='Field Name')
    field_name = fields.Char(string='Field')
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
