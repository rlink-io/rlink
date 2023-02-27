from odoo import api, models, fields, _
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, ValidationError
import locale
import base64
import pandas as pd
import io
from bs4 import BeautifulSoup

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


class ProjectTasksDynamicReport(models.Model):
    _name = 'project.tasks.dynamic.reports'
    _description = 'Project Tasks Dynamic Reports'
    display_name = fields.Char(default='Project Tasks Dynamic Reports')

    from_date = fields.Date(string='From Date')
    to_date = fields.Date(string='To Date')

    user_ids = fields.Many2many('res.users', string='Employees')
    task_ids = fields.Many2many('project.task', string='Tasks', compute='_compute_task_ids')
    report = fields.Many2one('ir.attachment')

    @api.depends('from_date', 'to_date', 'user_ids')
    def _compute_task_ids(self):
        done_stages = self.env['project.task.type'].search([('name', '=', 'Done')]).ids
        all_tasks = self.env['project.task'].search([('stage_id', 'in', done_stages)])
        task_ids = []
        for task in all_tasks:
            for user_id in self.user_ids:
                if user_id.id in task.user_ids.ids \
                        and self.from_date <= task.date_last_stage_update.date() <= self.to_date:
                    task_ids.append(task.id)

        self.task_ids = [(6, 0, task_ids)]

    def export_excel(self):
        if self.task_ids:
            output = io.BytesIO()
            writer = pd.ExcelWriter(output, engine='xlsxwriter')
            workbook = writer.book
            header_format = workbook.add_format({'bold': True})
            main_worksheet = workbook.add_worksheet("Dynamic Tasks Report")
            main_worksheet.set_column(0, 10, 20)
            main_worksheet.merge_range(0, 0, 1, 0, "Project", header_format)
            main_worksheet.merge_range(0, 1, 1, 1, "Assignees", header_format)
            main_worksheet.merge_range(0, 2, 1, 2, "Task Name", header_format)
            main_worksheet.merge_range(0, 3, 0, 4, "Planned Date", header_format)
            main_worksheet.write(1, 3, "From", header_format)
            main_worksheet.write(1, 4, "TO", header_format)
            main_worksheet.merge_range(0, 5, 1, 5, "Description", header_format)
            main_worksheet.merge_range(0, 6, 1, 6, "Time sheet", header_format)
            main_worksheet.merge_range(0, 7, 0, 9, "Assessments", header_format)
            main_worksheet.write(1, 7, "Speed", header_format)
            main_worksheet.write(1, 8, "Quality", header_format)
            main_worksheet.write(1, 9, "No Repeated Errors", header_format)

            main_worksheet.merge_range(0, 10, 1, 10, "Stage", header_format)

            row = 2
            for task in self.task_ids:
                main_worksheet.write(row, 0, task.project_id.name, header_format)
                assignees = ', '.join(user.name for user in task.user_ids)
                main_worksheet.write(row, 1, assignees, header_format)
                main_worksheet.write(row, 2, task.name, header_format)
                main_worksheet.write(row, 3, task.planned_date_from.strftime('%m/%d/%Y') if task.planned_date_from else '', header_format)
                main_worksheet.write(row, 4, task.planned_date_to.strftime('%m/%d/%Y') if task.planned_date_to else '', header_format)
                desc = ' '.join(BeautifulSoup(task.description, "html.parser").stripped_strings)
                main_worksheet.write(row, 5, desc, header_format)
                main_worksheet.write(row, 6, task.effective_hours, header_format)
                main_worksheet.write(row, 7, task.speed, header_format)
                main_worksheet.write(row, 8, task.quality, header_format)
                main_worksheet.write(row, 9, task.no_repeated_errors, header_format)
                main_worksheet.write(row, 10, task.stage_id.name, header_format)
                row = row + 1
            workbook.close()
            data = base64.encodestring(output.getvalue())

            file_name = "Dynamic Tasks Report.xlsx"
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

            base_url = self.env['ir.config_parameter'].get_param('web.base.url')
            download_url = '/web/content/' + str(self.report.id) + '?download=true'
            return {
                "type": "ir.actions.act_url",
                "url": str(download_url),
                "target": "self",
            }
            report.unlink()

        else:
            pass
