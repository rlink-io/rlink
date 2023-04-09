from odoo import api, models, fields, _
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, ValidationError
import locale
import base64
import pandas as pd
import io
import math
from bs4 import BeautifulSoup

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


def get_time_from_float(float_number):
    factor = float_number < 0 and -1 or 1
    val = abs(float_number)
    time_tuple = (factor * int(math.floor(val)), int(round((val % 1) * 60)))
    return time_tuple


class ProjectTimesheetReports(models.Model):
    _name = 'project.timesheet.reports'
    _description = 'Project Timesheet Reports'
    display_name = fields.Char(default='Project Timesheet Reports')

    from_date = fields.Date(string='From Date')
    to_date = fields.Date(string='To Date')

    employee_ids = fields.Many2many('hr.employee', string='Employees')
    timesheet_ids = fields.Many2many('account.analytic.line', string='Timesheet', compute='_compute_timesheet_ids')
    report = fields.Many2one('ir.attachment')

    @api.depends('from_date', 'to_date', 'employee_ids')
    def _compute_timesheet_ids(self):
        domain = [('employee_id', 'in', self.employee_ids.ids),
                  ('task_id', '!=', False),
                  ('project_id', '!=', False),
                  ('date', '>=', self.from_date),
                  ('date', '<', self.to_date),
                  ]
        timesheet_ids = self.env['account.analytic.line'].search(domain)
        self.timesheet_ids = [(6, 0, timesheet_ids.ids)]

    def export_excel(self):
        if self.timesheet_ids:
            output = io.BytesIO()
            writer = pd.ExcelWriter(output, engine='xlsxwriter')
            workbook = writer.book
            header_format = workbook.add_format({'bold': True})
            header_format.set_align('center')
            header_format.set_align('vcenter')
            main_worksheet = workbook.add_worksheet("Project Timesheet Report")
            main_worksheet.set_column(0, 6, 20)
            main_worksheet.merge_range(0, 0, 1, 0, "Project", header_format)
            main_worksheet.merge_range(0, 1, 1, 1, "Task Name", header_format)
            main_worksheet.merge_range(0, 2, 1, 2, "Assignee", header_format)
            main_worksheet.merge_range(0, 3, 0, 5, "Timesheet", header_format)
            main_worksheet.write(1, 3, "Date", header_format)
            main_worksheet.write(1, 4, "Description", header_format)
            main_worksheet.write(1, 5, "Hours Spent", header_format)
            row = 2
            for timesheet in self.timesheet_ids:
                main_worksheet.write(row, 0, timesheet.project_id.name)
                main_worksheet.write(row, 1, timesheet.task_id.name)
                main_worksheet.write(row, 2, timesheet.employee_id.name)
                main_worksheet.write(row, 3, timesheet.date.strftime('%m/%d/%Y'))
                main_worksheet.write(row, 4, timesheet.name)
                main_worksheet.write(row, 5, ':'.join(map(str, get_time_from_float(timesheet.unit_amount))))

                row = row + 1
            workbook.close()
            data = base64.encodestring(output.getvalue())

            file_name = "Project Timesheets Report.xlsx"
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
            self.report = report

            download_url = '/web/content/' + str(self.report.id) + '?download=true'
            return {
                "type": "ir.actions.act_url",
                "url": str(download_url),
                "target": "self",
            }
            report.unlink()

        else:
            pass
