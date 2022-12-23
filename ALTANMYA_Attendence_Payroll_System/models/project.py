from odoo import api, models, fields, _
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError


class ProjectInherited(models.Model):
    _inherit = 'project.project'

    @api.model
    def create(self, vals):
        rec = super(ProjectInherited, self).create(vals)
        to_do = self.env['project.task.type'].search([('name', '=', 'To Do')], limit=1)
        doing = self.env['project.task.type'].search([('name', '=', 'Doing')], limit=1)
        to_check = self.env['project.task.type'].search([('name', '=', 'To Check')], limit=1)
        done = self.env['project.task.type'].search([('name', '=', 'Done')], limit=1)
        if not to_do:
            to_do = self.env['project.task.type'].create({'name': 'To Do', 'sequence': 1})
        if not doing:
            doing = self.env['project.task.type'].create({'name': 'Doing', 'sequence': 2})
        if not to_check:
            to_check = self.env['project.task.type'].create({'name': 'To Check', 'sequence': 3})
        if not done:
            done = self.env['project.task.type'].create({'name': 'Done', 'sequence': 4})
        type_ids = [to_do.id, doing.id, to_check.id, done.id]
        rec.type_ids = type_ids
        return rec


class ProjectTaskInherited(models.Model):
    _inherit = 'project.task'

    speed = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'),
                              ('4', '4'), ('5', '5')], string='Speed')
    quality = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'),
                                ('4', '4'), ('5', '5')], string='Quality')
    no_repeated_errors = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'),
                                           ('4', '4'), ('5', '5')], string='No Repeated Error')
    requested_by = fields.Many2many('res.users', readonly=True, related='user_ids', string="Requested By")
    department_id = fields.Many2one('hr.department', compute="_compute_department_id", store=True)
    description = fields.Html(required=True)
    planned_date_from = fields.Date("Start date")
    planned_date_to = fields.Date("End date")

    planned_date_begin = fields.Datetime("Start date", tracking=True, task_dependency_tracking=True,
                                         compute="_compute_planned_date_begin")
    planned_date_end = fields.Datetime("End date", compute="_compute_planned_date_end")

    @api.depends('planned_date_from')
    def _compute_planned_date_begin(self):
        for rec in self:
            if rec.planned_date_from:
                date = rec.planned_date_from
                rec.planned_date_begin = datetime(date.year, date.month, date.day, 21, 0, 0) - timedelta(
                    days=1)
            else:
                rec.planned_date_begin = False

    @api.depends('planned_date_to')
    def _compute_planned_date_end(self):
        for rec in self:
            if rec.planned_date_to:
                date = rec.planned_date_to
                rec.planned_date_end = datetime(date.year, date.month, date.day, 21, 0, 0) - timedelta(days=1)
            else:
                rec.planned_date_end = False

    @api.constrains('description')
    def _check_len_html(self):
        print(self.description, len(self.description))
        if len(self.description) < 25 + 7:
            raise ValidationError("Description should be more than 25 character")

    @api.depends('user_ids')
    def _compute_department_id(self):
        for rec in self:
            rec.department_id = False
            if rec.user_ids:
                for user_id in rec.user_ids:
                    if user_id.employee_id:
                        if user_id.employee_id.department_id:
                            rec.department_id = user_id.employee_id.department_id.id
                            break


class account_analytic_line_inherited(models.Model):
    _inherit = 'account.analytic.line'

    @api.constrains('name')
    def _check_name_len(self):
        if len(self.name) < 25:
            raise ValidationError(
                "The Description of timesheet line cannot be empty and should be more than 25 characters.")


class ReportProjectTaskUserInherited(models.Model):
    _inherit = "report.project.task.user"
    department_id = fields.Many2one('hr.department', readonly=True, string="Department")

    def _select(self):
        return super()._select() + ", t.department_id"

    def _group_by(self):
        return super()._group_by() + ", t.department_id"
