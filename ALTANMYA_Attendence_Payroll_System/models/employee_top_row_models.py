from odoo import api, models, fields, _


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
            violation.display_name ="Violation"

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


class Training(models.Model):
    _name = "hr.training"
    _description = 'Training'

    display_name = fields.Char(compute='_compute_display_name')
    training_type = fields.Selection([('internal', 'Internal'), ('external', 'External')], string="Training Type")
    hours = fields.Integer(string=" Hours")
    cost = fields.Monetary(string="Cost")
    trainer = fields.Char(string="Trainer")
    training_party = fields.Many2one('res.partner')
    employee_id = fields.Many2one('hr.employee', required=True)
    company_id = fields.Many2one('res.company', related='employee_id.company_id', readonly=False,
                                 default=lambda self: self.env.company, required=True)
    currency_id = fields.Many2one(string="Currency", related='company_id.currency_id', readonly=True)

    @api.model
    def create(self, vals):
        new = super(Training, self).create(vals)
        new.employee_id.training_id = new.id
        return new

    def _compute_display_name(self):
        for training in self:
            training.display_name = _("%s\'s Training", training.employee_id.name)


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
