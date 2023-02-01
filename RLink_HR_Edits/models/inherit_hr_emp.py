from odoo import api, models, fields, _
import xlsxwriter
import time
import os
import base64
import pandas as pd
import io
from odoo.fields import Command
import datetime
from io import BytesIO
from urllib.request import urlopen
from odoo.tools.image import image_data_uri


class ExtendEmp(models.Model):
    _inherit = 'hr.employee'
    # _name = 'attendance.employee'

    father_name = fields.Char(string='Father\'s Name')
    mother_name = fields.Char(string='Mother\'s Name')
    landline_number = fields.Char(string='Landline Number')
    military_status = fields.Selection([('served', 'Served'), ('not_served', 'Not Served'),
                                        ('exempted', 'Exempted'), ('not_applicable', 'Not Applicable')])
    insurance_card_number = fields.Char(string='Insurance Card Number')
    bank_account_number = fields.Char(string='Bank Account NO.')
    deduction_ids = fields.One2many('hr.deduction', 'employee_id')
    violation_ids = fields.One2many('hr.violation', 'employee_id')
    bonus_ids = fields.One2many('hr.bonus', 'employee_id')
    training_ids = fields.One2many('hr.training', 'employee_id')
    days_off_id = fields.Many2one('hr.days.off')
    salary_raise_ids = fields.One2many('hr.salary.raise', 'employee_id')
    rotation_ids = fields.One2many('hr.rotation', 'employee_id')
    assessment_id = fields.Many2one('hr.assessment')
    state = fields.Selection([('confirmation_needed', 'Confirmation Needed'), ('confirmed', 'Confirmed')],
                             default='confirmed')
    change_request = fields.One2many('hr.change.request', 'employee_id')
    emp_report = fields.Many2one('ir.attachment')
    employee_att = fields.Binary(string='Employee Attachment')
    emp_image = fields.Binary(string='Image Attachment')

    @api.model
    def create(self, vals):
        new = super(ExtendEmp, self).create(vals)
        employees = self.env['hr.employee'].search([])
        for employee in employees:
            if not employee.assessment_id:
                assessment = self.env['hr.assessment'].sudo().create({
                    "employee_id": employee.id
                })
                points_report = self.env['points.credit.report'].sudo().create({"assessment_id": assessment.id})
                api_report = self.env['kpi.monthly.report'].sudo().create({"assessment_id": assessment.id})

            if not employee.days_off_id:
                days_off = self.env['hr.days.off'].sudo().create({
                    "employee_id": employee.id
                })
        return new

    def unlink(self):
        self.assessment_id.sudo().unlink()
        self.days_off_id.sudo().unlink()
        return super(ExtendEmp, self).unlink()

    def write(self, values):
        # if 'assessment_id' in values:
        #     rec = super(ExtendEmp, self).write(values)
        if not self.env.user.has_group('hr.group_hr_manager') and self.user_id.state != 'new':
            self.create_change_request(values)
            rec = super(ExtendEmp, self).write({'state': 'confirmation_needed'})
        else:
            if 'job_title' in values or 'department_id' in values:
                new_title = values['job_title'] if 'job_title' in values else self.job_title
                new_dep = self.env['hr.department'].sudo().search([('id', '=', values['department_id'])],
                                                                  limit=1).id if 'department_id' in values else self.department_id.id
                self.create_rotation(new_title, new_dep)
            rec = super(ExtendEmp, self).write(values)
        return rec

    def create_rotation(self, new_title, new_dep):
        self.env['hr.rotation'].sudo().create(
            {'employee_id': self.id,
             'date': str(datetime.datetime.now().date()),
             'old_title': self.job_title,
             'new_title': new_title,
             'old_department': self.department_id.id if self.department_id else '',
             'new_department': new_dep})

    def _check_employees_birthdays_cron(self):
        all_employees = self.env['hr.employee'].search([])
        notification_date = str((datetime.datetime.now() + datetime.timedelta(days=3)).date())
        for emp in all_employees:
            if str(emp.birthday)[4:] == notification_date[4:]:
                message = "{name} birthday in {date}".format(name=emp.name, date=str(emp.birthday))
                self.send_message_to_hr_employees_channel(message)
                self.send_private_message_to_hr_manager(message)

    def check_emp_continuous_employment(self, employee):
        continuous_employment = True
        sorted_contracts = employee.contract_ids.sorted(key=lambda r: r.date_start)
        first_contract = sorted_contracts[0]
        for i, contract_id in enumerate(sorted_contracts):
            if i != len(sorted_contracts) - 1:
                if sorted_contracts[i + 1].date_start and contract_id.date_end:
                    if (sorted_contracts[i + 1].date_start - contract_id.date_end).days != 1:
                        continuous_employment = False
                        break
                else:
                    continuous_employment = False
        return continuous_employment, first_contract

    def _check_permanent_job_date_cron(self):
        all_employees = self.env['hr.employee'].search([])
        notification_date = str((datetime.datetime.now() + datetime.timedelta(days=10)).date())
        for emp in all_employees:
            if emp.contract_ids and len(emp.contract_ids) > 1:
                is_continuous_employment, first_contract = self.check_emp_continuous_employment(emp)
                if is_continuous_employment:
                    permanent_start_date = first_contract.permanent_period_start_date
                    if str(permanent_start_date) == notification_date:
                        message = "{name} should get his permanent job in {date} according to {contract}".format(
                            name=emp.name, date=str(permanent_start_date), contract=first_contract.name,
                        )
                        self.send_message_to_hr_employees_channel(message)
                        self.send_private_message_to_hr_manager(message)

                if not is_continuous_employment and emp.contract_id:
                    permanent_start_date = emp.contract_id.permanent_period_start_date

                    if str(permanent_start_date) == notification_date:
                        message = "{name} should get his permanent job in {date} according to {contract}".format(
                            name=emp.name, date=str(permanent_start_date), contract=emp.contract_id.name
                        )
                        self.send_message_to_hr_employees_channel(message)
                        self.send_private_message_to_hr_manager(message)

    def _check_employee_contract_end_date_cron(self):
        all_employees = self.env['hr.employee'].search([])
        notification_date = str((datetime.datetime.now() + datetime.timedelta(days=7)).date())
        for emp in all_employees:
            if emp.contract_id:
                contract_id = emp.contract_id
                if str(contract_id.date_end) == notification_date:
                    message = "{name} current contract will expire in {date} ".format(
                        name=emp.name, date=str(contract_id.date_end))
                    self.send_message_to_hr_employees_channel(message)
                    self.send_private_message_to_hr_manager(message)

    def _check_employee_anniversary_cron(self):
        all_employees = self.env['hr.employee'].search([])
        notification_date = str((datetime.datetime.now() + datetime.timedelta(days=5)).date())
        for emp in all_employees:
            if emp.contract_ids and len(emp.contract_ids) > 1:
                is_continuous_employment, first_contract = self.check_emp_continuous_employment(emp)
                if is_continuous_employment:
                    probation_start_date = first_contract.probation_period_start_date
                    if str(probation_start_date)[4:] == notification_date[4:] and \
                            int(str(probation_start_date)[:4]) < int(notification_date[:4]):
                        message = "{name}\'s anniversary in {date} according to {contract}".format(
                            name=emp.name, date=str(notification_date), contract=first_contract.name)
                        self.send_message_to_hr_employees_channel(message)
                        self.send_private_message_to_hr_manager(message)

                if not is_continuous_employment and emp.contract_id:
                    probation_start_date = emp.contract_id.probation_period_start_date
                    if str(probation_start_date)[4:] == notification_date[4:] and \
                            int(str(probation_start_date)[:4]) < int(notification_date[:4]):
                        message = "{name}\'s anniversary in {date} according to {contract} ".format(name=emp.name,
                                                                                                    date=str(
                                                                                                        notification_date),
                                                                                                    contract=emp.contract_id.name)
                        self.send_message_to_hr_employees_channel(message)
                        self.send_private_message_to_hr_manager(message)

    def send_private_message_to_hr_manager(self, message):
        users = self.env.ref('hr.group_hr_manager').users
        for user in users:
            channel = self.env['mail.channel'].channel_get(
                [user.partner_id.id])
            channel_id = self.env['mail.channel'].browse(channel["id"])
            channel_id.message_post(
                body=message,
                message_type='comment',
                subtype_xmlid='mail.mt_comment',
            )

    def send_message_to_hr_employees_channel(self, message):
        hr_employees_group = self.env.ref('ALTANMYA_Attendence_Payroll_System.group_hr_employees')
        hr_emp_channel_id = self.env['mail.channel'].search(
            [('group_public_id', 'in', [hr_employees_group.id])])
        notification_ids = [((0, 0, {
            'res_partner_id': self.env.user.id,
            'notification_type': 'inbox'}))]
        user_id = self.env.user.id
        hr_emp_channel_id.message_post(author_id=user_id,
                                       body=message,
                                       message_type='notification',
                                       subtype_xmlid="mail.mt_comment",
                                       notification_ids=notification_ids,
                                       notify_by_email=True,
                                       )

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

            if field_name != 'departure_description' and previous_value != new_value and self.id:
                self.env['hr.change.request'].create({
                    'employee_id': self.id,
                    'field_type': field_type,
                    'field_label': self._fields[val].string if self._fields[val].string else self._fields[val],
                    'field_name': field_name,
                    'previous_value_origin': self[val],
                    'previous_value': previous_value,
                    'new_value_origin': values[val],
                    'new_value': new_value
                })

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

    def call_deductions_action(self):

        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("ALTANMYA_Attendence_Payroll_System.hr_deduction_action")
        action['context'] = dict(self._context, default_employee_id=self.id, )
        action['domain'] = [('employee_id', '=', self.id)]
        return action

    def call_rotation_action(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("ALTANMYA_Attendence_Payroll_System.hr_rotation_action")
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
        if not self.days_off_id:
            self.env['hr.days.off'].sudo().create({
                "employee_id": self.id
            })

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

    def action_export_excel(self):
        domain = []
        if self.env.context.get('active_ids'):
            domain = [('id', 'in', self.env.context.get('active_ids', []))]

        self = self.env['hr.employee'].search(domain, limit=1)
        output = io.BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        workbook = writer.book
        header_format = workbook.add_format({'bold': True})
        sub_title_format = workbook.add_format({'bg_color': '#E5E4E2', 'bold': True})
        main_worksheet = workbook.add_worksheet("Employee's Information")
        training_worksheet = workbook.add_worksheet("Training")
        violations_worksheet = workbook.add_worksheet("Violations")
        bonuses_worksheet = workbook.add_worksheet("Bonuses")
        salary_raise_worksheet = workbook.add_worksheet("Salary Raise")
        deductions_worksheet = workbook.add_worksheet("Deductions")
        evaluation_worksheet = workbook.add_worksheet("Evaluation")
        rotation_worksheet = workbook.add_worksheet("Rotation")

        main_worksheet.set_column(0, 1, 30)

        self.fill_main_worksheet_data(main_worksheet, header_format, sub_title_format)
        self.fill_training_worksheet_data(training_worksheet, header_format)
        self.fill_violation_worksheet_data(violations_worksheet, header_format)
        self.fill_bonuses_worksheet_data(bonuses_worksheet, header_format)
        self.fill_salary_raise_worksheet_data(salary_raise_worksheet, header_format)
        self.fill_deductions_worksheet_data(deductions_worksheet, header_format)
        self.fill_evaluation_worksheet_data(evaluation_worksheet, header_format)
        self.fill_rotation_worksheet_data(rotation_worksheet, header_format)
        workbook.close()
        data = base64.encodestring(output.getvalue())

        file_name = "{name} Report {date}.xlsx".format(name=self.name, date=time.strftime("%Y-%m-%d"))
        attachment = {
            'name': file_name,
            'store_fname': file_name,
            'datas': data,
            'res_id': self.id,
            'res_model': self._name,
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            'type': 'binary'
        }
        report = self.env['ir.attachment'].create(attachment)
        self.emp_report = report

        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        download_url = '/web/content/' + str(self.emp_report.id) + '?download=true'
        return {
            "type": "ir.actions.act_url",
            "url": str(base_url) + str(download_url),
            "target": "self",
        }
        report.unlink()

    def get_main_worksheet_data(self):
        main_worksheet_data = (['Employee Image', self.image_1920],
                               ['Employee Name', self.name], ['Job Title', self.job_title],
                               ['Tags', ' - '.join([str(tag.name) for tag in self.category_ids])],
                               ['Work Mobile', self.mobile_phone],
                               ['Mobile Phone', self.work_phone],
                               ['Work Email', self.work_email],
                               ['Company', self.company_id.name],
                               ['Department', self.department_id.name],
                               ['Manager', self.parent_id.name],
                               ['Work Information', 'sub-title'],
                               ['Location', 'sub-title'],
                               ['Work Address',
                                self.address_id.name],
                               ['Work Location', self.work_location_id.name],
                               # ['Approves', 'sub-title'],
                               # ['Leave Manager', self.leave_manager_id.name],
                               ['Schedule', 'sub-title'],
                               ['Working Hours', self.resource_calendar_id.name],
                               ['Timezone', self.tz],
                               ['Private Information', 'sub-title'],
                               ['Address', self.address_home_id.name],
                               ['Email', self.private_email],
                               ['Phone', self.phone],
                               ['Landline Number', self.landline_number],
                               ['Bank Account Number',
                                self.bank_account_id.acc_number + ((
                                                                           ' - ' + self.bank_account_id.bank_id.name) if self.bank_account_id.bank_id else '') if self.bank_account_id else ""],
                               ['Home-Work Distance', str(self.km_home_work) + ' km'],
                               ['Emergency', 'sub-title'],
                               ['Emergency Contact', self.emergency_contact],
                               ['Emergency Phone', self.emergency_phone],
                               ['Education', 'sub-title'],
                               ['Certificate Level', dict(self._fields['certificate'].selection).get(self.certificate)],
                               ['Field of Study', self.study_field],
                               ['School', self.study_school],
                               ['Citizenship', 'sub-title'],
                               ['Nationality (Country)', self.country_id.name],
                               ['Identification No', self.identification_id],
                               ['Passport No', self.passport_id],
                               ['Military Status',
                                dict(self._fields['military_status'].selection).get(self.military_status)],
                               ['Father\'s Name', self.father_name],
                               ['Mother\'s Name', self.mother_name],
                               ['Father\'s Name', self.father_name],
                               ['Gender', dict(self._fields['gender'].selection).get(self.gender)],
                               ['Date of Birth', self.birthday.strftime('%m/%d/%Y') if self.birthday else ''],
                               ['Place of Birth', self.place_of_birth],
                               ['Country of Birth', self.country_of_birth.name],
                               ['Marital Status', 'sub-title'],
                               # print dict(self._fields['marital'].selection).get(self.marital)
                               ['Marital Status', dict(self._fields['marital'].selection).get(self.marital)],
                               ['Spouse Complete Name',
                                self.spouse_complete_name if self.marital not in ['single', 'widower',
                                                                                  'divorced'] else ''],
                               ['Spouse Birthdate',
                                self.spouse_birthdate.strftime(
                                    '%m/%d/%Y') if self.spouse_birthdate and self.marital not in ['single',
                                                                                                  'widower',
                                                                                                  'divorced'] else ''],
                               ['Dependent', 'sub-title'],
                               ['Number of Children', self.children],
                               ['Work Permit', 'sub-title'],
                               ['Visa No', self.visa_no],
                               ['Work Permit No', self.permit_no],
                               ['Visa Expire Date', self.visa_expire.strftime('%m/%d/%Y') if self.visa_expire else ''],
                               ['Work Permit Expiration Date', self.work_permit_expiration_date.strftime(
                                   '%m/%d/%Y') if self.work_permit_expiration_date else ''],

                               ['HR Setting', 'sub-title'],
                               ['Status', 'sub-title'],
                               ['Employee Type', self.employee_type],
                               ['First Contract Date',
                                self.first_contract_date.strftime('%m/%d/%Y') if self.first_contract_date else ''],
                               ['Related User', self.user_id.name],
                               ['Attendance/Point of Sale', 'sub-title'],
                               ['PIN Code', self.pin],
                               ['Attendance Mode', dict(self._fields['att_mode'].selection).get(self.att_mode)],
                               ['Id on device', self.studio_employee_number],
                               ['Badge ID', self.barcode],
                               ['Payroll', 'sub-title'],
                               ['Current Contract', self.contract_id.name],
                               ['Job Position', self.job_id.name],
                               ['Registration Number of the Employee', self.registration_number],
                               ['Insurance Card Number', self.insurance_card_number],
                               ['Bank Account NO.', self.bank_account_number],
                               ['Employee Files', 'sub-title'],
                               ['Image Attachment', self.emp_image],

                               )
        return main_worksheet_data

    def fill_main_worksheet_data(self, main_worksheet, header_format, sub_title_format):
        sub_title_format.set_align('center')
        main_worksheet_data = self.get_main_worksheet_data()
        row = 0
        col = 0
        for item, value in main_worksheet_data:
            if value == 'sub-title':
                main_worksheet.merge_range(row, col, row, col + 1, item, sub_title_format)
                # main_worksheet.write(row, col, item, sub_title_format)
            else:
                main_worksheet.write(row, col, item, header_format)
            if not value or value == 'sub-title':
                value = ''
            if item in ['Employee Image', 'Image Attachment'] and value:
                url = image_data_uri(value)
                image_data = BytesIO(urlopen(url).read())
                main_worksheet.insert_image(row, col + 2, url, {'image_data': image_data})
            else:
                main_worksheet.write(row, col + 1, value)
            row += 1

    def fill_training_worksheet_data(self, training_worksheet, header_format):
        training_worksheet.set_column(0, 4, 15)
        training_worksheet.write(0, 0, 'Training Type', header_format)
        training_worksheet.write(0, 1, 'Hours', header_format)
        training_worksheet.write(0, 2, ' Cost', header_format)
        training_worksheet.write(0, 3, 'Trainer', header_format)
        training_worksheet.write(0, 4, 'Training Entity', header_format)
        if self.training_ids:
            row = 1
            for training in self.training_ids:
                training_worksheet.write(row, 0, training.training_type if training.training_type else '')
                training_worksheet.write(row, 1, training.hours)
                training_worksheet.write(row, 2, training.cost)
                training_worksheet.write(row, 3, training.trainer if training.trainer else '')
                training_worksheet.write(row, 4, training.training_entity.name if training.training_entity else '')
                row = row + 1

    def fill_violation_worksheet_data(self, violation_worksheet, header_format):
        violation_worksheet.set_column(0, 2, 15)
        violation_worksheet.write(0, 0, 'Violation Type', header_format)
        violation_worksheet.write(0, 1, 'Violation Reason', header_format)
        violation_worksheet.write(0, 2, ' Violation Date', header_format)
        if self.violation_ids:
            row = 1
            for violation in self.violation_ids:
                violation_worksheet.write(row, 0, violation.violation_type if violation.violation_type else '')
                violation_worksheet.write(row, 1, violation.reason if violation.reason else '')
                violation_worksheet.write(row, 2, violation.date.strftime('%m/%d/%Y') if violation.date else '')
                row = row + 1

    def fill_bonuses_worksheet_data(self, bonuses_worksheet, header_format):
        bonuses_worksheet.set_column(0, 2, 15)
        bonuses_worksheet.write(0, 0, 'Bonus Reason', header_format)
        bonuses_worksheet.write(0, 1, 'Bonus Date', header_format)
        bonuses_worksheet.write(0, 2, 'Bonus Value', header_format)
        if self.bonus_ids:
            row = 1
            for bonus in self.bonus_ids:
                bonuses_worksheet.write(row, 0, bonus.reason if bonus.reason else '')
                bonuses_worksheet.write(row, 1, bonus.date.strftime('%m/%d/%Y') if bonus.date else '')
                bonuses_worksheet.write(row, 2, bonus.value)
                row = row + 1

    def fill_salary_raise_worksheet_data(self, salary_raise_worksheet, header_format):
        salary_raise_worksheet.set_column(0, 2, 15)
        salary_raise_worksheet.write(0, 0, 'Raise Reason', header_format)
        salary_raise_worksheet.write(0, 1, 'Raise Value', header_format)
        salary_raise_worksheet.write(0, 2, 'Raise Date', header_format)
        if self.salary_raise_ids:
            row = 1
            for salary_raise_id in self.salary_raise_ids:
                salary_raise_worksheet.write(row, 0, salary_raise_id.reason if salary_raise_id.reason else '')
                salary_raise_worksheet.write(row, 1, salary_raise_id.fixed_raise_value)
                salary_raise_worksheet.write(row, 2,
                                             salary_raise_id.date.strftime('%m/%d/%Y') if salary_raise_id.date else '')

                row = row + 1

    def fill_deductions_worksheet_data(self, deductions_worksheet, header_format):
        deductions_worksheet.set_column(0, 2, 15)
        deductions_worksheet.write(0, 0, 'Deduction Reason', header_format)
        deductions_worksheet.write(0, 1, 'Deduction Value', header_format)
        deductions_worksheet.write(0, 2, 'Deduction Date', header_format)
        if self.deduction_ids:
            row = 1
            for deduction_id in self.deduction_ids:
                deductions_worksheet.write(row, 0, deduction_id.reason if deduction_id.reason else '')
                deductions_worksheet.write(row, 1, deduction_id.value)
                deductions_worksheet.write(row, 2,
                                           deduction_id.date.strftime('%m/%d/%Y') if deduction_id.date else '')
                row = row + 1

    def fill_evaluation_worksheet_data(self, evaluation_worksheet, header_format):
        evaluation_worksheet.set_column(0, 2, 15)
        evaluation_worksheet.write(0, 0, 'Year', header_format)
        evaluation_worksheet.write(0, 1, ' month', header_format)
        evaluation_worksheet.write(0, 2, 'Account', header_format)
        evaluation_worksheet.write(0, 3, 'KPI', header_format)
        evaluation_worksheet.write(0, 4, 'Training', header_format)
        evaluation_worksheet.write(0, 5, 'Evaluation', header_format)
        evaluation_worksheet.write(0, 6, 'Total', header_format)
        row = 1
        evaluation_rows = self.env['points.report.row'].search(
            [('report_id', '=', self.assessment_id.points_report_id.id)])
        if evaluation_rows:
            for table_row in evaluation_rows:
                evaluation_worksheet.write(row, 0, table_row.eval_year)
                evaluation_worksheet.write(row, 1, table_row.eval_month)
                evaluation_worksheet.write(row, 2, table_row.account)
                evaluation_worksheet.write(row, 3, table_row.eval_kpi)
                evaluation_worksheet.write(row, 4, table_row.training)
                evaluation_worksheet.write(row, 5, table_row.evaluation)
                evaluation_worksheet.write(row, 6, table_row.eval_total)
                row = row + 1

    def fill_rotation_worksheet_data(self, rotation_worksheet, header_format):
        rotation_worksheet.set_column(0, 6, 15)
        rotation_worksheet.write(0, 0, 'Rotation Date', header_format)
        rotation_worksheet.write(0, 1, 'Old Title', header_format)
        rotation_worksheet.write(0, 2, 'New Title', header_format)
        rotation_worksheet.write(0, 3, 'Old Department', header_format)
        rotation_worksheet.write(0, 4, 'New Department', header_format)
        rotation_worksheet.write(0, 5, 'Old Salary', header_format)
        rotation_worksheet.write(0, 6, 'New Salary', header_format)

        row = 1
        rotation_rows = self.env['hr.rotation'].sudo().search(
            [('employee_id', '=', self.id)])
        if rotation_rows:
            for rotation_row in rotation_rows:
                rotation_worksheet.write(row, 0, rotation_row.date.strftime('%m/%d/%Y') if rotation_row else '')
                rotation_worksheet.write(row, 1, rotation_row.old_title if rotation_row.old_title else '')
                rotation_worksheet.write(row, 2, rotation_row.new_title if rotation_row.new_title else '')
                rotation_worksheet.write(row, 3,
                                         rotation_row.old_department.name if rotation_row.old_department else '')
                rotation_worksheet.write(row, 4,
                                         rotation_row.new_department.name if rotation_row.new_department else '')
                rotation_worksheet.write(row, 5, rotation_row.old_salary)
                rotation_worksheet.write(row, 6, rotation_row.new_salary)
                row = row + 1

    def _update_hr_employees_group_users_cron(self):

        all_employees = self.env['hr.employee'].search([])
        hr_employees_group = self.env.ref('ALTANMYA_Attendence_Payroll_System.group_hr_employees')
        for emp in all_employees:
            if emp.user_id and emp.user_id.has_group('hr.group_hr_manager'):
                hr_employees_group.write({'users': [(4, emp.user_id.id)]})
            else:
                hr_department = self.env['hr.department'].search([('name', '=', 'Human Resources')])
                if hr_department and emp.department_id and emp.user_id:
                    if emp.department_id.id == hr_department.id and not emp.user_id.has_group(
                            'ALTANMYA_Attendence_Payroll_System.group_hr_employees'):
                        hr_employees_group.write({'users': [(4, emp.user_id.id)]})
                    elif emp.department_id.id != hr_department.id and emp.user_id.has_group(
                            'ALTANMYA_Attendence_Payroll_System.group_hr_employees'):
                        hr_employees_group.write({'users': [(3, emp.user_id.id)]})
                        self.remove_user_from_hr_employee_channel(emp.user_id)

    def remove_user_from_hr_employee_channel(self, user_id):
        hr_employees_channel = self.env.ref('ALTANMYA_Attendence_Payroll_System.channel_hr_employee')
        channel_member = self.env['mail.channel.partner'].sudo().search([
            ('partner_id', '=', user_id.partner_id.id),
            ('channel_id', '=', hr_employees_channel.id),
        ])
        hr_employees_channel.sudo().write({'channel_last_seen_partner_ids': [(3, channel_member.id)]})


class ExtendEmpPub(models.Model):
    _inherit = 'hr.employee.public'
    # _name = 'attendance.employee'

    father_name = fields.Char(string='Father\'s Name')
    mother_name = fields.Char(string='Mother\'s Name')
    landline_number = fields.Char(string='Landline Number')
    military_status = fields.Selection([('served', 'Served'), ('not_served', 'Not Served'),
                                        ('exempted', 'Exempted'), ('not_applicable', 'Not Applicable')])
    insurance_card_number = fields.Char(string='Insurance Card Number')
    bank_account_number = fields.Char(string='Bank Account NO.')
    deduction_ids = fields.One2many('hr.deduction', 'employee_id')
    violation_ids = fields.One2many('hr.violation', 'employee_id')
    bonus_ids = fields.One2many('hr.bonus', 'employee_id')
    training_ids = fields.One2many('hr.training', 'employee_id')
    days_off_id = fields.Many2one('hr.days.off')
    salary_raise_ids = fields.One2many('hr.salary.raise', 'employee_id')
    rotation_ids = fields.One2many('hr.rotation', 'employee_id')
    assessment_id = fields.Many2one('hr.assessment')
    state = fields.Selection([('confirmation_needed', 'Confirmation Needed'), ('confirmed', 'Confirmed')],
                             default='confirmed')
    change_request = fields.One2many('hr.change.request', 'employee_id')
    emp_report = fields.Many2one('ir.attachment')
    # employee_att = fields.Binary(string='Employee Attachment')
    # emp_image = fields.Binary(string='Image Attachment')
