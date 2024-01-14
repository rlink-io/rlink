from odoo import api, models, fields, _
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, ValidationError
import locale
import logging
from dateutil.relativedelta import relativedelta
import datetime

_logger = logging.getLogger(__name__)

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


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
    date = fields.Datetime('Date')

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
            # if task.date_check:
            #     if user_id in task.user_ids.ids \
            #             and task.date_check.month == yesterday_date.month \
            #             and task.date_check.year == yesterday_date.year:
            #                 task_number = task_number + 1
            #                 task.task_number = task_number
            #                 task.total = ((int(task.speed) * 1.5) + (int(task.quality) * 2) + (
            #                     int(task.no_repeated_errors))) / 4.5
            #                 sum_total += task.total
            #                 task_ids.append(task.id)
            # elif not task.date_check:
            if task.planned_date_to:
                if user_id in task.user_ids.ids \
                        and task.planned_date_to.month == yesterday_date.month \
                        and task.planned_date_to.year == yesterday_date.year:
                            task_number = task_number + 1
                            task.task_number = task_number
                            task.total = ((int(task.speed) * 1.5) + (int(task.quality) * 2) + (
                                int(task.no_repeated_errors))) / 4.5
                            sum_total += task.total
                            task_ids.append(task.id)
        if task_ids:
            monthly_total = sum_total / len(task_ids)

        return task_ids, monthly_total

    def compute_task_ids_month(self, user_id, i):
       

        yesterday_date = date.today() - relativedelta(months=i)
        done_stages = self.env['project.task.type'].search([('name', '=', 'Done')]).ids
        all_task = self.env['project.task'].search([('stage_id', 'in', done_stages)])
        task_number = 0
        sum_total = 0
        monthly_total = 0
        task_ids = []
        for task in all_task:
            if task.planned_date_to:
                if user_id in task.user_ids.ids \
                        and task.planned_date_to.month == yesterday_date.month \
                        and task.planned_date_to.year == yesterday_date.year:
                    task_number = task_number + 1
                    task.task_number = task_number
                    task.total = ((int(task.speed) * 1.5) + (int(task.quality) * 2) + (
                        int(task.no_repeated_errors))) / 4.5
                    sum_total += task.total
                    task_ids.append(task.id)
        if task_ids:
            monthly_total = sum_total / len(task_ids)

        return task_ids, monthly_total

    def _create_monthly_project_employee_report_cron1(self):

        all_users = self.env['res.users'].sudo().search([('share', '=', False)])
        yesterday_date = date.today() - timedelta(days=1)
        _logger.info(f'sdswwwwwwwwwwwwww{yesterday_date}')

        for user in all_users:
            task_ids, monthly_total = self.compute_task_ids(user.id)
            _logger.info(f'fffffffffffffff{task_ids, monthly_total}')
            vals = {
                'user_id': user.id,
                'month': str(yesterday_date.month),
                'year': yesterday_date.year,
                'task_ids': task_ids,
                'total': monthly_total,
                'date':datetime.datetime.strptime("1/"+str(yesterday_date.month)+"/"+str(yesterday_date.year),'%d/%m/%Y')
            }
            self.sudo().fill_Kpi_in_employees_reports(user, yesterday_date, monthly_total)
            _logger.info(
                f'aqqqqqqqqqqqqqqqqqqq{self.sudo().fill_Kpi_in_employees_reports(user, yesterday_date, monthly_total)}')

            self.env['project.employees.reports'].sudo().create(vals)

    def _create_monthly_project_employee_report_cron1_month(self):
        
        all_users = self.env['res.users'].sudo().search([('share', '=', False)])

        for i in range(1, 12):
            yesterday_date = date.today() - relativedelta(months=i)
            for user in all_users:
                task_ids, monthly_total = self.sudo().compute_task_ids_month(user.id, i)
                vals = {
                    'user_id': user.id,
                    'month': str(yesterday_date.month),
                    'year':str(yesterday_date.year),
                    'task_ids': task_ids,
                    'total': monthly_total,
                    'date':datetime.datetime.strptime("1/"+str(yesterday_date.month)+"/"+str(yesterday_date.year),'%d/%m/%Y')
                }
                self.sudo().fill_Kpi_in_employees_reports(user, yesterday_date, monthly_total)

                self.env['project.employees.reports'].sudo().create(vals)

    def fill_Kpi_in_employees_reports(self, user, yesterday_date, monthly_total):
        if user.employee_ids:
            for employee_id in user.employee_ids:
                kpi_report_id = self.env['kpi.monthly.report'].search([('employee_id', '=', employee_id.id)],
                                                                      limit=1)
                print(kpi_report_id)
                for row_id in kpi_report_id.rows_ids:

                    if (row_id['year'] == str(yesterday_date.year) and row_id['month'] == yesterday_date.strftime(
                            "%B")):
                        row_id.sudo().kpi = monthly_total

                points_report_id = self.env['points.credit.report'].search([('employee_id', '=', employee_id.id)],
                                                                           limit=1)
                for row_id in points_report_id.rows_ids:
                    if (row_id['eval_year'] == str(yesterday_date.year) and row_id[
                        'eval_month'] == yesterday_date.strftime(
                        "%B")):
                        row_id.sudo().eval_kpi = monthly_total
