from odoo import api, models, fields, _
from datetime import datetime
from odoo.exceptions import UserError, ValidationError


class Deduction(models.Model):
    _name = "hr.deduction"
    _description = 'Deduction'

    display_name = fields.Char(compute='_compute_display_name')
    reason = fields.Char(string="Deduction Reason")
    date = fields.Date(string="Deduction Date")
    value = fields.Monetary(string="Deduction Value")
    employee_id = fields.Many2one('hr.employee', required=True)
    company_id = fields.Many2one('res.company', related='employee_id.company_id', readonly=False,
                                 default=lambda self: self.env.company, required=True)
    currency_id = fields.Many2one(string="Currency", related='company_id.currency_id', readonly=True)

    def _compute_display_name(self):
        for deduction in self:
            employee_deductions_count = self.env['hr.deduction'].search_count(
                [('employee_id', '=', deduction.employee_id.id)])
            deduction.display_name = "Deduction {count}".format(count=employee_deductions_count)

    def write(self, vals):
        if 'value' in vals and vals['value'] < 0:
            raise ValidationError('You can\'t enter negative value for deduction value')
        else:
            return super(Deduction, self).write(vals)

    @api.model
    def create(self, vals_list):
        if 'value' in vals_list and vals_list['value'] < 0:
            raise ValidationError('You can\'t enter negative value for deduction value')
        else:
            return super(Deduction, self).create(vals_list)


class Violation(models.Model):
    _name = "hr.violation"
    _description = 'Violation'

    violation_type = fields.Char(string="Violation Type")
    reason = fields.Char(string="Violation Reason")
    date = fields.Date(string="Violation Date")
    employee_id = fields.Many2one('hr.employee', required=True)


class Bonus(models.Model):
    _name = "hr.bonus"
    _description = 'Employee Bonuses'

    # display_name = fields.Char(compute='_compute_display_name')
    reason = fields.Char(string="Bonus Reason")
    date = fields.Date(string="Bonus Date")
    value = fields.Monetary(string="Bonus Value")
    employee_id = fields.Many2one('hr.employee', required=True)
    company_id = fields.Many2one('res.company', related='employee_id.company_id', readonly=False,
                                 default=lambda self: self.env.company, required=True)
    currency_id = fields.Many2one(string="Currency", related='company_id.currency_id', readonly=True)

    # def _compute_display_name(self):
    #     for bonus in self:
    #         employee_bonuses_count = self.env['hr.bonus'].search_count(
    #             [('employee_id', '=', bonus.employee_id.id)])
    #         bonus.display_name = "Bonus {count}".format(count=employee_bonuses_count)

    def write(self, vals):
        if 'value' in vals and vals['value'] < 0:
            raise ValidationError('You can\'t enter negative value for bonus value')
        else:
            return super(Bonus, self).write(vals)

    @api.model
    def create(self, vals_list):
        if 'value' in vals_list and vals_list['value'] < 0:
            raise ValidationError('You can\'t enter negative value for bonus value')
        else:
            return super(Bonus, self).create(vals_list)


class SalaryRaise(models.Model):
    _name = "hr.salary.raise"
    _description = 'Employee Salary Raise'

    display_name = fields.Char(compute='_compute_display_name')
    reason = fields.Char(string="Raise Reason")
    raise_value_type = fields.Selection([('fixed_value', 'Fixed Value'), ('percentage_value', 'Percentage Value')],
                                        string='Raise Value Type', required=True)
    raise_value = fields.Monetary(string="Raise Value")
    fixed_raise_value = fields.Char(string="Raise Value", compute='_compute_fixed_raise_value')
    date = fields.Date(string="Raise Date")
    employee_id = fields.Many2one('hr.employee', required=True)
    company_id = fields.Many2one('res.company', related='employee_id.company_id', readonly=False,
                                 default=lambda self: self.env.company, required=True)
    currency_id = fields.Many2one(string="Currency", related='company_id.currency_id', readonly=True)

    def _compute_display_name(self):
        for salary_raise in self:
            employee_raises_count = self.env['hr.salary.raise'].search_count(
                [('employee_id', '=', salary_raise.employee_id.id)])
            salary_raise.display_name = "Salary Raise {count}".format(count=employee_raises_count)

    @api.depends('raise_value_type', 'raise_value')
    def _compute_fixed_raise_value(self):
        for salary_raise in self:
            if salary_raise.raise_value_type == 'fixed_value':
                salary_raise.fixed_raise_value = str(salary_raise.raise_value) + str(salary_raise.currency_id.symbol)
            else:
                salary_raise.fixed_raise_value = str(salary_raise.raise_value) + '%'

    def write(self, vals):
        if 'raise_value' in vals and vals['raise_value'] < 0:
            raise ValidationError('You can\'t enter negative value for Raise Value')

        else:
            return super(SalaryRaise, self).write(vals)

    @api.model
    def create(self, vals_list):
        if 'raise_value' in vals_list and vals_list['raise_value'] < 0:
            raise ValidationError('You can\'t enter negative value for Raise Value')
        else:
            return super(SalaryRaise, self).create(vals_list)


class Training(models.Model):
    _name = "hr.training"
    _description = 'Training'

    training_type = fields.Selection([('internal', 'Internal'), ('external', 'External')], string="Training Type")
    hours = fields.Integer(string=" Hours")
    cost = fields.Monetary(string="Cost")
    trainer = fields.Char(string="Trainer")
    training_entity = fields.Many2one('res.partner', string='Training Entity', required=True)
    employee_id = fields.Many2one('hr.employee', required=True)
    company_id = fields.Many2one('res.company', related='employee_id.company_id', readonly=False,
                                 default=lambda self: self.env.company, required=True)
    currency_id = fields.Many2one(string="Currency", related='company_id.currency_id', readonly=True)

    def write(self, vals):
        if 'hours' in vals and vals['hours'] < 0:
            raise ValidationError('You can\'t enter negative value for Hours')
        elif 'cost' in vals and vals['cost'] < 0:
            raise ValidationError('You can\'t enter negative value for Cost')
        else:
            return super(Training, self).write(vals)

    @api.model
    def create(self, vals_list):
        if 'hours' in vals_list and vals_list['hours'] < 0:
            raise ValidationError('You can\'t enter negative value for hours')
        elif 'cost' in vals_list and vals_list['cost'] < 0:
            raise ValidationError('You can\'t enter negative value for cost')
        else:
            return super(Training, self).create(vals_list)


class Rotation(models.Model):
    _name = 'hr.rotation'

    employee_id = fields.Many2one('hr.employee', required=True)
    date = fields.Date(string='Rotation Date')
    old_title = fields.Char(string='Old Title')
    new_title = fields.Char(string='New Title')
    old_department = fields.Many2one('hr.department', string='Old Department')
    new_department = fields.Many2one('hr.department', string="New Department")
    old_salary = fields.Monetary(string='Old Salary')
    new_salary = fields.Monetary(string='New Salary')
    company_id = fields.Many2one('res.company', related='employee_id.company_id', readonly=False,
                                 default=lambda self: self.env.company, required=True)
    currency_id = fields.Many2one(string="Currency", related='company_id.currency_id', readonly=True)

    def write(self, vals):
        if 'old_salary' in vals and vals['old_salary'] < 0:
            raise ValidationError('You can\'t enter negative value for old salary')
        elif 'new_salary' in vals and vals['new_salary'] < 0:
            raise ValidationError('You can\'t enter negative value for new salary')
        else:
            return super(Rotation, self).write(vals)

    @api.model
    def create(self, vals_list):
        if 'old_salary' in vals_list and vals_list['old_salary'] < 0:
            raise ValidationError('You can\'t enter negative value for old salary')
        elif 'new_salary' in vals_list and vals_list['new_salary'] < 0:
            raise ValidationError('You can\'t enter negative value for new salary')
        else:
            return super(Rotation, self).create(vals_list)


class DaysOff(models.Model):
    _name = "hr.days.off"
    _description = 'Employee Days off - paid time off leaves'

    employee_id = fields.Many2one('hr.employee', required=True)
    display_name = fields.Char(compute='_compute_display_name')
    total = fields.Float(string=" Total", compute='compute_total')
    used = fields.Float(string=" Used", compute='compute_total')
    remaining = fields.Float(string=" Remaining", compute='compute_total')

    @api.model
    def create(self, vals):
        new = super(DaysOff, self).create(vals)
        new.employee_id.days_off_id = new.id
        return new

    def _compute_display_name(self):
        for days_off in self:
            days_off.display_name = _("%s\'s days off", days_off.employee_id.name)

    @api.depends('employee_id')
    def compute_total(self):
        for rec in self:
            rec.total = rec.used = rec.remaining = 0.0
            all_allocations = self.env['hr.leave.allocation'].search(
                [('employee_id', '=', rec.employee_id.id), ('holiday_status_id', '=', 1)])
            if all_allocations:
                for allocation in all_allocations:
                    if allocation.date_from <= datetime.now().date() <= allocation.date_to:
                        rec.total = allocation.max_leaves
                        rec.used = allocation.leaves_taken
                        rec.remaining = allocation.max_leaves - allocation.leaves_taken
                        break


class Assessment(models.Model):
    _name = "hr.assessment"
    _description = 'Employee Assessment'

    display_name = fields.Char(compute='_compute_display_name')
    employee_id = fields.Many2one('hr.employee', required=True)
    points_report_id = fields.Many2one('points.credit.report')
    kpi_report_id = fields.Many2one('kpi.monthly.report')

    @api.model
    def create(self, vals):
        new = super(Assessment, self).create(vals)
        new.employee_id.assessment_id = new.id

        kpi_report = self.env['kpi.monthly.report'].sudo().create({"assessment_id": new.id, })
        new.kpi_report_id = kpi_report.id

        points_report = self.env['points.credit.report'].sudo().create({
            "assessment_id": new.id,
        })
        new.points_report_id = points_report.id
        return new

    def open_points_credit_report(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id(
            "ALTANMYA_Attendence_Payroll_System.points_credit_report_action")

        action['context'] = dict(self._context, default_assessment_id=self.id)
        action['domain'] = [('assessment_id', '=', self.id)]
        if self.points_report_id:
            action['res_id'] = self.points_report_id.id
        return action

    def open_kpi_monthly_report(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id(
            "ALTANMYA_Attendence_Payroll_System.kpi_monthly_report_action")
        action['context'] = dict(self._context, default_assessment_id=self.id)
        action['domain'] = [('assessment_id', '=', self.id)]
        if self.kpi_report_id:
            action['res_id'] = self.kpi_report_id.id
        return action

    def _compute_display_name(self):
        for assessment in self:
            assessment.display_name = _("%s\'s assessment", assessment.employee_id.name)


class KPIMonthlyReport(models.Model):
    _name = 'kpi.monthly.report'
    _description = 'KPI Monthly Report'

    @api.model
    def year_selection(self):
        year = 2022
        year_list = []
        while year != 2043:
            year_list.append((str(year), str(year)))
            year += 1
        return year_list

    @api.model
    def filter_rows(self):
        domain = []
        years_list = ['2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033',
                      '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042']
        months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                       'October', 'November', 'December']

        if self.filter_by == 'year':
            if self.year:
                domain = [("year", "=", self.year)]

        elif self.filter_by == 'year_and_month' and self.from_year and self.to_year and self.from_month and self.to_month:
            if int(self.from_year) > int(self.to_year):
                domain = [('id', '=', '0')]
            elif self.from_year == self.to_year:
                if months_list.index(self.from_month) > months_list.index(self.to_month):
                    domain = [('id', '=', '0')]
                else:
                    months_range = months_list[months_list.index(self.from_month):months_list.index(self.to_month) + 1]
                    domain = [('month', 'in', months_range), ('year', '=', self.from_year)]
            elif int(self.from_year) < int(self.to_year):
                from_months_list = months_list[months_list.index(self.from_month):]
                to_months_list = months_list[:months_list.index(self.to_month) + 1]
                domain = ['|', (
                    'year', 'in', years_list[years_list.index(self.from_year) + 1:years_list.index(self.to_year)]),
                          '|', '&', ('month', 'in', from_months_list), ('year', '=', self.from_year),
                          '&', ('month', 'in', to_months_list), ('year', '=', self.to_year)]
        return domain

    display_name = fields.Char(default='Kpi Monthly Report')
    assessment_id = fields.Many2one('hr.assessment', required=True, ondelete='cascade')
    employee_id = fields.Many2one('hr.employee', related='assessment_id.employee_id', required=True)
    filter_by = fields.Selection([('year', 'Year'), ('year_and_month', 'Year And Month')],
                                 default='year',
                                 string='Filter By')
    from_year = fields.Selection(
        year_selection,
        string="Year",

    )
    to_year = fields.Selection(
        year_selection,
        string="Year",

    )
    year = fields.Selection(
        year_selection,
        string="Year",

    )
    from_month = fields.Selection([('January', 'January'), ('February', 'February'),
                                   ('March', 'March'), ('April', 'April'),
                                   ('May', 'May'), ('June', 'June'),
                                   ('July', 'July'), ('August', 'August'),
                                   ('September', 'September'), ('October', 'October'),
                                   ('November', 'November'), ('December', 'December')], string='From')
    to_month = fields.Selection([('January', 'January'), ('February', 'February'),
                                 ('March', 'March'), ('April', 'April'),
                                 ('May', 'May'), ('June', 'June'),
                                 ('July', 'July'), ('August', 'August'),
                                 ('September', 'September'), ('October', 'October'),
                                 ('November', 'November'), ('December', 'December')],
                                string='To')

    rows_ids = fields.One2many('kpi.report.row', 'report_id', domain=filter_rows)

    @api.model
    def create(self, vals):
        new = super(KPIMonthlyReport, self).create(vals)

        months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                       'October', 'November', 'December']
        current_month = datetime.now().month
        for month in months_list[current_month - 1:]:
            KPI_report_row = self.env['kpi.report.row'].create({
                "report_id": new.id,
                "month": month,
                "year": str(datetime.now().year),

            })
        return new

    def _yearly_update_monthly_kpi_report_cron(self):
        KPI_report_ids = self.env['kpi.monthly.report'].search([])
        for KPI_report_id in KPI_report_ids:
            KPI_report_id.year = str(datetime.now().year)
            months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                           'September',
                           'October', 'November', 'December']
            for month in months_list:
                new_row = self.env['kpi.report.row'].sudo().create({
                    "report_id": KPI_report_id.id,
                    "year": str(datetime.now().year),
                    "month": month,
                })


class KPIReportRow(models.Model):
    _name = 'kpi.report.row'
    _description = 'KPI Monthly Report Row'

    @api.model
    def year_selection(self):
        year = 2022
        year_list = []
        while year != 2043:
            year_list.append((str(year), str(year)))
            year += 1
        return year_list

    report_id = fields.Many2one('kpi.monthly.report', required=True, ondelete="cascade")
    year = fields.Selection(
        year_selection,
        string="Year",
        required=True
    )
    month = fields.Selection([('January', 'January'), ('February', 'February'),
                              ('March', 'March'), ('April', 'April'),
                              ('May', 'May'), ('June', 'June'),
                              ('July', 'July'), ('August', 'August'),
                              ('September', 'September'), ('October', 'October'),
                              ('November', 'November'), ('December', 'December')],
                             required=True, string='Month')

    kpi = fields.Integer(string='KPI', default=0)
    is_hr_manager = fields.Boolean(compute="_compute_is_hr_manager", default=False)

    def _compute_is_hr_manager(self):
        for rec in self:
            if self.env.user.has_group('hr.group_hr_manager'):
                rec.is_hr_manager = True
            else:
                rec.is_hr_manager = False


class PointsCreditReport(models.Model):
    _name = 'points.credit.report'
    _description = 'Points Credit Report'

    @api.model
    def year_selection(self):
        year = 2022
        year_list = []
        while year != 2043:
            year_list.append((str(year), str(year)))
            year += 1
        return year_list

    @api.model
    def filter_rows(self):
        domain = []
        years_list = ['2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033',
                      '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042']
        months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                       'October', 'November', 'December']

        if self.filter_by == 'year':
            if self.year:
                domain = [("eval_year", "=", self.year)]

        elif self.filter_by == 'year_and_month' and self.from_year and self.to_year and self.from_month and self.to_month:
            if int(self.from_year) > int(self.to_year):
                domain = [('id', '=', '0')]
            elif self.from_year == self.to_year:
                if months_list.index(self.from_month) > months_list.index(self.to_month):
                    domain = [('id', '=', '0')]
                else:
                    months_range = months_list[months_list.index(self.from_month):months_list.index(self.to_month) + 1]
                    domain = [('eval_month', 'in', months_range), ('eval_year', '=', self.from_year)]
            elif int(self.from_year) < int(self.to_year):
                from_months_list = months_list[months_list.index(self.from_month):]
                to_months_list = months_list[:months_list.index(self.to_month) + 1]
                domain = ['|', (
                    'eval_year', 'in', years_list[years_list.index(self.from_year) + 1:years_list.index(self.to_year)]),
                          '|', '&', ('eval_month', 'in', from_months_list), ('eval_year', '=', self.from_year),
                          '&', ('eval_month', 'in', to_months_list), ('eval_year', '=', self.to_year)]
        return domain

    @api.model
    def get_current_round_limit(self):
        reports = self.env['points.report.row'].search(
            [('eval_year', '=', str(datetime.now().year)), ('month_number', '=', datetime.now().month)])
        if reports:
            return reports[0].round_limit_row
        else:
            return 5

    display_name = fields.Char(default='Points Credit Report')
    assessment_id = fields.Many2one('hr.assessment', 'points_report_id', required=True, ondelete='cascade')
    employee_id = fields.Many2one('hr.employee', related='assessment_id.employee_id', required=True)
    round_limit = fields.Integer(string='Current Round Limit', required=True,
                                 default=get_current_round_limit)  # for Hr manager
    current_round_limit = fields.Integer(string='Current Round Limit', required=True, default=get_current_round_limit)
    is_hr_manager_profile = fields.Boolean(compute="_compute_is_hr_manager_profile", default=False)

    filter_by = fields.Selection([('year', 'Year'), ('year_and_month', 'Year And Month')],
                                 default='year',
                                 string='Filter By')
    from_year = fields.Selection(
        year_selection,
    )
    to_year = fields.Selection(
        year_selection,
    )
    year = fields.Selection(
        year_selection,
        string="Year",
    )
    from_month = fields.Selection([('January', 'January'), ('February', 'February'),
                                   ('March', 'March'), ('April', 'April'),
                                   ('May', 'May'), ('June', 'June'),
                                   ('July', 'July'), ('August', 'August'),
                                   ('September', 'September'), ('October', 'October'),
                                   ('November', 'November'), ('December', 'December')], string='From')
    to_month = fields.Selection([('January', 'January'), ('February', 'February'),
                                 ('March', 'March'), ('April', 'April'),
                                 ('May', 'May'), ('June', 'June'),
                                 ('July', 'July'), ('August', 'August'),
                                 ('September', 'September'), ('October', 'October'),
                                 ('November', 'November'), ('December', 'December')],
                                string='To')
    rows_ids = fields.One2many('points.report.row', 'report_id', domain=filter_rows)

    def _compute_is_hr_manager_profile(self):
        for rec in self:
            if rec.employee_id.user_id and rec.employee_id.user_id.has_group('hr.group_hr_manager'):
                rec.is_hr_manager_profile = True
            else:
                rec.is_hr_manager_profile = False

    @api.model
    def create(self, vals):
        new = super(PointsCreditReport, self).create(vals)

        months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                       'October', 'November', 'December']
        current_month = datetime.now().month
        for month in months_list[current_month - 1:]:
            points_report_row = self.env['points.report.row'].sudo().create({
                "account": 0,
                "report_id": new.id,
                "eval_month": month,
                "eval_year": str(datetime.now().year),
                "month_number": months_list.index(month) + 1,
                "round_limit_row": new.current_round_limit})
        return new

    def write(self, vals):
        if 'round_limit' in vals and vals['round_limit'] < 0:
            raise ValidationError('you can\'t enter negative value for Round Limit')

        else:
            rec = super(PointsCreditReport, self).write(vals)
            if 'round_limit' in vals:
                self.update_reports_current_round_limit(vals['round_limit'])
                self.update_reports_rows_round_limit(vals['round_limit'])
            return rec

    def update_reports_current_round_limit(self, new_round_limit):

        points_report_ids = self.env['points.credit.report'].search([])
        for report in points_report_ids:
            report.write({'current_round_limit': new_round_limit})

    def update_reports_rows_round_limit(self, new_round_limit):
        current_year = datetime.now().year
        current_month = datetime.now().month
        updated_rows = self.env['points.report.row'].search(
            [('eval_year', '=', current_year), ('month_number', '>=', current_month)])
        for row in updated_rows:
            row.round_limit_row = new_round_limit
            row.compute_account_value()

    def _yearly_update_points_credit_report_cron(self):
        points_report_ids = self.env['points.credit.report'].search([])
        for points_report_id in points_report_ids:
            months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                           'September',
                           'October', 'November', 'December']
            for month in months_list:
                self.env['points.report.row'].sudo().create({
                    "account": 0,
                    "report_id": points_report_id.id,
                    "eval_month": month,
                    "eval_year": str(datetime.now().year),
                    "month_number": months_list.index(month) + 1,
                    "round_limit_row": points_report_id.current_round_limit})


class points_report_row(models.Model):
    _name = 'points.report.row'
    _description = 'Points Credit Report Row'

    @api.model
    def year_selection(self):
        year = 2022
        year_list = []
        while year != 2043:
            year_list.append((str(year), str(year)))
            year += 1
        return year_list

    report_id = fields.Many2one('points.credit.report', required=True, ondelete="cascade")
    eval_month = fields.Selection([('January', 'January'), ('February', 'February'),
                                   ('March', 'March'), ('April', 'April'),
                                   ('May', 'May'), ('June', 'June'),
                                   ('July', 'July'), ('August', 'August'),
                                   ('September', 'September'), ('October', 'October'),
                                   ('November', 'November'), ('December', 'December')],
                                  required=True, string='Month')
    month_number = fields.Integer()
    eval_year = fields.Selection(
        year_selection,
        string="Year",
        required=True
    )
    account = fields.Integer(string='Account')
    eval_kpi = fields.Integer(string='KPI')
    evaluation = fields.Integer(string='Evaluation')
    training = fields.Integer(string='Training')
    eval_total = fields.Integer(string='Total', compute='_compute_total')
    round_limit_row = fields.Integer(string='Round Limit')
    is_hr_manager = fields.Boolean(compute="_compute_is_hr_manager", default=False)

    def _compute_is_hr_manager(self):
        for rec in self:
            if self.env.user.has_group('hr.group_hr_manager'):
                rec.is_hr_manager = True
            else:
                rec.is_hr_manager = False

    @api.onchange('eval_total')
    def compute_account_value(self):
        years_list = ['2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033',
                      '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042']
        domain_year = str(int(self.eval_year) + 1) if self.month_number == 12 else self.eval_year
        next_years = years_list[years_list.index(self.eval_year) + 1:]
        domain = [("report_id", "=", self.report_id._origin.id),
                  '|', '&', ("month_number", ">", self.month_number), ("eval_year", "=", domain_year),
                  ("eval_year", "in", next_years)
                  ]
        next_rows = self.env['points.report.row'].search(domain)
        if next_rows:
            for i, next_row in enumerate(next_rows):
                previous_row_total = self.eval_total if i == 0 else next_rows[i - 1].eval_total
                next_row.account = previous_row_total - self.round_limit_row if self.round_limit_row < previous_row_total else 0

    @api.onchange('account')
    def check_training_value(self):
        if self.account < 0:
            raise ValidationError('you can\'t enter negative value for account value')

    @api.onchange('eval_kpi')
    def check_eval_kpi_value(self):
        if self.eval_kpi < 0:
            raise ValidationError('you can\'t enter negative value for KPI value')

    @api.onchange('training')
    def check_training_value(self):
        if self.training < 0:
            raise ValidationError('you can\'t enter negative value for training value')

    @api.onchange('evaluation')
    def check_evaluation_value(self):
        if self.evaluation < 0:
            raise ValidationError('you can\'t enter negative value for evaluation value')

    @api.onchange('eval_total')
    def check_eval_total_value(self):
        if self.eval_total < 0:
            raise ValidationError('you can\'t enter negative value for total value')

    @api.depends('account', 'eval_kpi', 'evaluation', 'training')
    def _compute_total(self):
        for row in self:
            row.eval_total = row.account + row.eval_kpi + row.evaluation + row.training
