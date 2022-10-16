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

    @api.depends('employee_id.name')
    def _compute_display_name(self):
        for deduction in self:
            deduction.display_name = "Deduction"

    @api.onchange('value')
    def check_deduction_value(self):
        if self.value < 0:
            raise ValidationError('You can\'t enter negative value for deduction value')


class Violation(models.Model):
    _name = "hr.violation"
    _description = 'Violation'

    display_name = fields.Char(compute='_compute_display_name')
    violation_type = fields.Char(string="Violation Type")
    reason = fields.Char(string="Violation Reason")
    date = fields.Date(string="Violation Date")
    employee_id = fields.Many2one('hr.employee', required=True)

    @api.depends('employee_id.name')
    def _compute_display_name(self):
        for violation in self:
            violation.display_name = "Violation"


class Bonus(models.Model):
    _name = "hr.bonus"
    _description = 'Employee Bonuses'

    display_name = fields.Char(compute='_compute_display_name')
    reason = fields.Char(string="Bonus Reason")
    date = fields.Date(string="Bonus Date")
    value = fields.Monetary(string="Bonus Value")
    employee_id = fields.Many2one('hr.employee', required=True)
    company_id = fields.Many2one('res.company', related='employee_id.company_id', readonly=False,
                                 default=lambda self: self.env.company, required=True)
    currency_id = fields.Many2one(string="Currency", related='company_id.currency_id', readonly=True)

    @api.depends('employee_id.name')
    def _compute_display_name(self):
        for bonus in self:
            bonus.display_name = "Bonus"

    @api.onchange('value')
    def check_bonus_value(self):
        if self.value < 0:
            raise ValidationError('You can\'t enter negative value for Bonus Value')


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

    @api.depends('employee_id.name')
    def _compute_display_name(self):
        for salary_raise in self:
            salary_raise.display_name = "Salary Raise"

    @api.depends('raise_value_type', 'raise_value')
    def _compute_fixed_raise_value(self):
        for salary_raise in self:
            if salary_raise.raise_value_type == 'fixed_value':
                salary_raise.fixed_raise_value = str(salary_raise.raise_value) + str(salary_raise.currency_id.symbol)
            else:
                salary_raise.fixed_raise_value = str(salary_raise.raise_value) + '%'

    @api.onchange('raise_value')
    def check_raise_value(self):
        if self.raise_value < 0:
            raise ValidationError('You can\'t enter negative value for Raise Value')


class Training(models.Model):
    _name = "hr.training"
    _description = 'Training'

    display_name = fields.Char(compute='_compute_display_name')
    training_type = fields.Selection([('internal', 'Internal'), ('external', 'External')], string="Training Type")
    hours = fields.Integer(string=" Hours")
    cost = fields.Monetary(string="Cost")
    trainer = fields.Char(string="Trainer")
    training_entity = fields.Many2one('res.partner', string='Training Entity', required=True)
    employee_id = fields.Many2one('hr.employee', required=True)
    company_id = fields.Many2one('res.company', related='employee_id.company_id', readonly=False,
                                 default=lambda self: self.env.company, required=True)
    currency_id = fields.Many2one(string="Currency", related='company_id.currency_id', readonly=True)

    def _compute_display_name(self):
        for training in self:
            training.display_name = _("%s\'s Training", training.employee_id.name)

    @api.onchange('hours')
    def check_hours_value(self):
        if self.hours < 0:
            raise ValidationError('You can\'t enter negative value for Hours')

    @api.onchange('cost')
    def check_cost_value(self):
        if self.cost < 0:
            raise ValidationError('You can\'t enter negative value for Cost')


class DaysOff(models.Model):
    _name = "hr.days.off"
    _description = 'Employee Days off'

    display_name = fields.Char(compute='_compute_display_name')
    total = fields.Integer(string=" Total")
    used = fields.Integer(string=" Used")
    remaining = fields.Integer(string=" Remaining")
    employee_id = fields.Many2one('hr.employee', required=True)

    @api.model
    def create(self, vals):
        new = super(DaysOff, self).create(vals)
        new.employee_id.days_off_id = new.id
        return new

    def _compute_display_name(self):
        for days_off in self:
            days_off.display_name = _("%s\'s days off", days_off.employee_id.name)


class Assessment(models.Model):
    _name = "hr.assessment"
    _description = 'Employee Assessment'

    display_name = fields.Char(compute='_compute_display_name')
    employee_id = fields.Many2one('hr.employee', required=True)
    evaluation_table_id = fields.Many2one('evaluation.table')
    tasks_table_rows_ids = fields.One2many('tasks.table', 'assessment_id')

    @api.model
    def create(self, vals):
        new = super(Assessment, self).create(vals)
        new.employee_id.assessment_id = new.id

        months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                       'October', 'November', 'December']
        for month in months_list:
            new_task_table_row = self.env['tasks.table'].create({
                "assessment_id": new.id,
                "year": datetime.now().year,
                "month": month
            })

        evaluation_table = self.env['evaluation.table'].sudo().create({
            "assessment_id": new.id,
        })
        new.evaluation_table_id = evaluation_table.id
        return new

    def open_evaluation_point_table(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id(
            "ALTANMYA_Attendence_Payroll_System.evaluation_table_action")
        action['context'] = dict(self._context, default_assessment_id=self.id)
        action['domain'] = [('assessment_id', '=', self.id)]
        if self.evaluation_table_id:
            action['res_id'] = self.evaluation_table_id.id
        return action

    def open_monthly_tasks_assessment_table(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("ALTANMYA_Attendence_Payroll_System.tasks_table_action")
        action['context'] = dict(self._context, default_assessment_id=self.id)
        action['domain'] = [('assessment_id', '=', self.id)]
        return action

    def _yearly_update_tasks_table_cron(self):
        all_assessments = self.env['hr.assessment'].search([])
        for assessment in all_assessments:
            months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                           'October', 'November', 'December']
            for month in months_list:
                new_row = self.env['tasks.table'].create({
                    "assessment_id": assessment.id,
                    "year": datetime.now().year,
                    "month": month
                })

    def _compute_display_name(self):
        for assessment in self:
            assessment.display_name = _("%s\'s assessment", assessment.employee_id.name)


class TasksTable(models.Model):
    _name = 'tasks.table'
    _description = 'Monthly Task Assessment Table'

    assessment_id = fields.Many2one('hr.assessment')
    employee_id = fields.Many2one('hr.employee', related='assessment_id.employee_id', required=True)
    year = fields.Char(string='Year')
    month = fields.Char(string='Month')
    kpi = fields.Integer(string='KPI', default=5)
    date = fields.Date(string='Date')


class EvaluationTable(models.Model):
    _name = 'evaluation.table'
    _description = 'Evaluation Point Table'

    display_name = fields.Char(default='Evaluation Point Table')
    assessment_id = fields.Many2one('hr.assessment', 'evaluation_table_id')
    employee_id = fields.Many2one('hr.employee', related='assessment_id.employee_id', required=True)
    round_limit = fields.Integer(string='Round Limit', default=5, required=True)
    from_month = fields.Selection([('January', 'January'), ('February', 'February'), ('March', 'March')
                                      , ('April', 'April'), ('May', 'May'), ('June', 'June'),
                                   ('July', 'July'), ('August', 'August'), ('September', 'September'),
                                   ('October', 'October'), ('November', 'November'), ('December', 'December')
                                   ], default='January')
    to_month = fields.Selection([('January', 'January'), ('February', 'February'), ('March', 'March')
                                    , ('April', 'April'), ('May', 'May'), ('June', 'June'),
                                 ('July', 'July'), ('August', 'August'), ('September', 'September'),
                                 ('October', 'October'), ('November', 'November'), ('December', 'December')
                                 ], default='December')
    rows_ids = fields.One2many('evaluation.table.row', 'table_id')
    filtered_ids = fields.Many2many('evaluation.table.row')

    @api.model
    def create(self, vals):
        new = super(EvaluationTable, self).create(vals)

        months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                       'October', 'November', 'December']
        for month in months_list:
            evaluation_table_row = self.env['evaluation.table.row'].create({
                "account": 0,
                "table_id": new.id,
                "month": month,
                "month_number": months_list.index(month) + 1})
        return new

    @api.onchange('round_limit')
    def _check_round_limit(self):
        if self.round_limit < 0:
            raise ValidationError('you can\'t enter negative value for Round Limit')

    @api.onchange('to_month', 'from_month')
    def _validate_months(self):
        months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                       'October', 'November', 'December']
        if months_list.index(self.from_month) > months_list.index(self.to_month):
            raise ValidationError('Please make sure that To Month value after From Month')
        else:
            months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                           'October', 'November', 'December']
            filtered_months = months_list[months_list.index(self.from_month):months_list.index(self.to_month) + 1]
            self.filtered_ids = self.env['evaluation.table.row'].search(
                [('table_id', '=', self._origin.id), ('month', 'in', filtered_months)])


class evaluation_table_row(models.Model):
    _name = 'evaluation.table.row'
    _description = 'Evaluation Point Table Row'

    table_id = fields.Many2one('evaluation.table')
    month = fields.Char(string='month')
    month_number = fields.Integer()
    account = fields.Integer(string='Account')
    kpi = fields.Integer(string='KPI')
    evaluation = fields.Integer(string='Evaluation')
    training = fields.Integer(string='Training')
    total = fields.Integer(string='Total', compute='_compute_total')
    round_limit_row = fields.Integer(string='Round Limit', default=0)

    @api.onchange('total')
    def compute_account_value(self):
        self.round_limit_row = self.table_id.round_limit
        domain = [("month_number", "=", self.month_number + 1), ("table_id", "=", self.table_id._origin.id)]
        next_row = self.env['evaluation.table.row'].search(domain)
        if next_row:
            next_row.account = self.total - self.round_limit_row
        else:
            domain = [("month_number", "=", 1), ("table_id", "=", self.table_id._origin.id)]
            first_row = self.env['evaluation.table.row'].search(domain)
            first_row.account = self.total - self.round_limit_row

    @api.onchange('training')
    def check_training_value(self):
        if self.training < 0:
            raise ValidationError('you can\'t enter negative value for training value')

    @api.onchange('evaluation')
    def check_evaluation_value(self):
        if self.evaluation < 0:
            raise ValidationError('you can\'t enter negative value for evaluation value')

    @api.depends('account', 'kpi', 'evaluation', 'training')
    def _compute_total(self):
        for row in self:
            row.total = row.account + row.kpi + row.evaluation + row.training
