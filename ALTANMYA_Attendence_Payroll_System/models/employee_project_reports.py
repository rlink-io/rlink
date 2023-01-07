from odoo import api, models, fields, _
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, ValidationError
import locale


class ProjectEmployeesReports(models.Model):
    _name = 'project.employees.reports'
    _description = 'Employees Reports'

    display_name = fields.Char(compute='_compute_display_name')
    user_id = fields.Many2one('res.users', string='Employee')
    month = fields.Selection([('1', 'January'), ('2', 'February'),
                              ('3', 'March'), ('4', 'April'),
                              ('5', 'May'), ('6', 'June'),
                              ('7', 'July'), ('8', 'August'),
                              ('9', 'September'), ('10', 'October'),
                              ('11', 'November'), ('12', 'December')],
                             required=True, string='Month')
    year = fields.Char(string='Year')
    total = fields.Float(string='Total', default=0)
    task_ids = fields.Many2many('project.task')

    def _compute_display_name(self):
        for report in self:
            report.display_name = "{user_name}-{month}-{year}".format(user_name=report.user_id.name,
                                                                      month=dict(report._fields['month'].selection).get(
                                                                          report.month),
                                                                      year=report.year)

    def compute_task_ids(self, user_id):
        yesterday_date = date.today() - timedelta(days=1)
        done_stages = self.env['project.task.type'].search([('name', '=', 'Done')]).ids
        all_task = self.env['project.task'].search([('stage_id', 'in', done_stages)])
        task_number = 0
        sum_total = 0
        monthly_total = 0
        task_ids = []
        for task in all_task:
            print(user_id, task.user_ids.ids)
            if user_id in task.user_ids.ids \
                    and task.date_last_stage_update.month == yesterday_date.month \
                    and task.date_last_stage_update.year == yesterday_date.year:
                task_number = task_number + 1
                task.task_number = task_number
                task.total = (int(task.speed) * 1.5 + int(task.quality) * 2 + int(task.no_repeated_errors)) / 4.5
                sum_total += task.total
                task_ids.append(task.id)
        if task_ids:
            monthly_total = sum_total / len(task_ids)

        return task_ids, monthly_total

    def _create_monthly_project_employee_report_cron(self):
        locale.setlocale(locale.LC_ALL, 'en_US')
        all_users = self.env['res.users'].sudo().search([('share', '=', False)])
        yesterday_date = date.today() - timedelta(days=1)
        print(yesterday_date.strftime("%B"))

        for user in all_users:
            task_ids, monthly_total = self.compute_task_ids(user.id)
            vals = {
                'user_id': user.id,
                'month': str(yesterday_date.month),
                'year': yesterday_date.year,
                'task_ids': task_ids,
                'total': monthly_total
            }
            self.fill_Kpi_in_employees_reports(user, yesterday_date, monthly_total)

            self.env['project.employees.reports'].sudo().create(vals)

    def fill_Kpi_in_employees_reports(self, user, yesterday_date, monthly_total):


        if user.employee_ids:
            for employee_id in user.employee_ids:
                kpi_report_id = self.env['kpi.monthly.report'].search([('employee_id', '=', employee_id.id)],
                                                                      limit=1)
                for row_id in kpi_report_id.rows_ids:
                    if (row_id['year'] == str(yesterday_date.year) and row_id['month'] == yesterday_date.strftime(
                            "%B")):
                        row_id.kpi = monthly_total

                points_report_id = self.env['points.credit.report'].search([('employee_id', '=', employee_id.id)],
                                                                           limit=1)
                for row_id in points_report_id.rows_ids:
                    if (row_id['eval_year'] == str(yesterday_date.year) and row_id[
                        'eval_month'] == yesterday_date.strftime(
                        "%B")):
                        row_id.eval_kpi = monthly_total
