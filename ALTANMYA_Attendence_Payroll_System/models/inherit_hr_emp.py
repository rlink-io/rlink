from odoo import api, models, fields


class ExtendEmp(models.Model):
    _inherit = 'hr.employee'
    # _name = 'attendance.employee'

    studio_employee_number = fields.Integer(string='Id on device')
    att_mode = fields.Selection([('standard', 'Standard mode'), ('daily', 'Daily mode'), ('classic', 'Classic mode'),
                                 ('sequential', 'Sequential mode'), ('shift', 'Shift mode')], string='Attendance Mode',
                                index=True)

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



