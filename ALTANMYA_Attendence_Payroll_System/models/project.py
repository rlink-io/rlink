from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError


class ProjectInherited(models.Model):
    _inherit = 'project.project'

    @api.model
    def create(self, vals_list):
        rec = super(ProjectInherited, self).create(vals_list)
        to_do = self.env['project.task.type'].search([('name', '=', 'To Do')], limit=1)
        doing = self.env['project.task.type'].search([('name', '=', 'Doing')], limit=1)
        to_check = self.env['project.task.type'].search([('name', '=', 'To Check')], limit=1)
        done = self.env['project.task.type'].search([('name', '=', 'DOne')], limit=1)
        if not to_do:
            to_do = self.env['project.task.type'].create({'name': 'To Do', 'sequence': 1})
        if not doing:
            doing = self.env['project.task.type'].create({'name': 'Doing', 'sequence': 2})
        if not to_check:
            to_check = self.env['project.task.type'].create({'name': 'To Check', 'sequence': 3})
        if not done:
            done = self.env['project.task.type'].create({'name': 'Done', 'sequence': 4})
        stages = [to_do.id, doing.id, to_check.id, done.id]
        rec.type_ids = stages
        return rec


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    name = fields.Char(string='Description', required=True)

    @api.constrains('name')
    def _check_name_length(self):
        for rec in self:
            if len(rec.name) < 25:
                raise ValidationError(
                    'The description of timesheet line is required and should be Minimum 25 characters')


class ProjectTaskInherited(models.Model):
    _inherit = 'project.task'

    # planned_date_begin = fields.Date()
    # planned_date_end = fields.Date()
    speed = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], string="Speed")
    quality = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], string="Quality")
    no_repeated_errors = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
                                          string="No Repeated Errors")
    requested_by = fields.Many2many('res.users', string="Requested By", related="user_ids", readonly=True)
    description = fields.Html(string="Description", required=True)

    @api.constrains('description')
    def _check_description_length(self):
        for rec in self:
            if len(rec.description) < 25+7:
                raise ValidationError(
                    'The description of task should be Minimum 25 characters')
