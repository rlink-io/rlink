from odoo import api, models, fields, _
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError
from bs4 import BeautifulSoup
import logging
_logger = logging.getLogger(__name__)
class ProjectTaskInherited(models.Model):
    _inherit = 'project.task'

    speed = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'),
                              ('4', '4'), ('5', '5')], string='Speed')
    quality = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'),
                                ('4', '4'), ('5', '5')], string='Quality')
    no_repeated_errors = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'),
                                           ('4', '4'), ('5', '5')], string='No Repeated Error')
    total = fields.Float(string='Total')
    task_number = fields.Integer(string='task.No')
    requested_by = fields.Many2one('res.users',
                                   string="Requested By")
    department_id = fields.Many2one('hr.department', compute="_compute_department_id", store=True)
    description = fields.Html(required=True)
    planned_date_from = fields.Date("Start date", required=True)
    planned_date_to = fields.Date("End date ", required=True)

    planned_date_begin = fields.Datetime("Start date", tracking=True, task_dependency_tracking=True,
                                         compute="_compute_planned_date_begin")
    planned_date_end = fields.Datetime("End date", compute="_compute_planned_date_end")
    direct_manager_id = fields.Many2one('res.users', compute="_compute_department_id", store=True)
    is_assessments_readonly = fields.Boolean(compute="_compute_is_assessments_readonly")
    notes_ids = fields.One2many('mail.message', 'res_id', string="Notes", domain=[('subtype_id', '!=', 1)])
    messages_ids = fields.One2many('mail.message', 'res_id', string='Messages', domain=[('subtype_id', '=', 1)])

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

    @api.constrains('timesheet_ids')
    def _check_timesheet_name_len(self):
        for rec in self:
            for timesheet in rec.timesheet_ids:
                print(timesheet.name, timesheet.document_attachment)
                if len(timesheet.name) < 25:
                    raise ValidationError(
                        "The Description of timesheet line cannot be empty and should be more than 25 characters.")
                optional_users_ids = self.env['project.users.management'].search([('id', '=', 1)]).optional_users.ids
               
                # if timesheet.employee_id.user_id.id not in optional_users_ids:
                #     raise ValidationError(
                #         "The Document in timesheet line is required.")

    @api.constrains('description')
    def _check_len_html(self):
        for rec in self:
            if rec.description:
                soup = BeautifulSoup(rec.description)
                soup_text = soup.text.replace('\n', ' ')
                if len(soup_text) < 25:
                    raise ValidationError("Description should be more than 25 character")

    def write(self, vals):
        if 'stage_id' in vals:
            self.check_stage_restrictions(vals)
        rec = super(ProjectTaskInherited, self).write(vals)
        if 'user_ids' in vals and 'requested_by' not in vals:
            for user_id in self.user_ids:
                if user_id.employee_id:
                    if user_id.employee_id.parent_id:
                        self.requested_by = user_id.employee_id.parent_id.user_id.id
                        break
        return rec

    @api.model
    def create(self, vals_list):
        
        if 'stage_id' in vals_list:
            _logger.info('ffferrrrrrrrrrrrrrrrrrrrrrrr')
            allow_employee = self.env['hr.employee'].sudo().search([('user_id','in',vals_list['user_ids'][0][2])])
            _logger.info(f'rrrrrrrrrrrrrrrrrrrrrrrr{allow_employee}')
            
           
            
            if self.env['project.task.type'].sudo().browse(vals_list['stage_id']).name == 'To Do' and(self.env.user.id != self.project_id.user_id.id or self.env.user.has_group('base.group_system')):
                
                raise ValidationError(
                        "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
        rec = super(ProjectTaskInherited, self).create(vals_list)
        
        if 'user_ids' in vals_list and not 'requested_by' in vals_list:
            
            
            for user_id in rec.user_ids:
                if user_id.employee_id:
                    if user_id.employee_id.parent_id:
                        rec.requested_by = user_id.employee_id.parent_id.user_id.id
                        break
        return rec

    def check_stage_restrictions(self, vals):
        all_approvers =[]
        all_approvers.append(self.direct_manager_id.id)
        if self.env.user.has_group('base.group_system'):
            all_approvers.append(self.env.user.id)
        if self.stage_id.name == 'Done' and not self.env.user.has_group('hr.group_hr_manager'):
            raise UserError(
                _("You are not allowed to change the stage of task please contact with the HR manager!"))
        if self.stage_id.name == 'Doing':
            new_stage = self.env['project.task.type'].search([('id', '=', vals['stage_id'])])
            if new_stage.name == "Done":
               raise UserError(
                        _("You are not allowed to change the stage of task please contact with the Direct Manager!"))     
        if self.stage_id.name == 'To Check':
            new_stage = self.env['project.task.type'].search([('id', '=', vals['stage_id'])])
            if new_stage.name == "Done":
                if self.env.user.id not in all_approvers:
                    
                    raise UserError(
                        _("You are not allowed to change the stage of task please contact with the Direct Manager!"))
                 
                else:
                    if not self.speed or not self.quality or not self.no_repeated_errors:
                        raise UserError(
                            _("Please fill the task assessments before moving it to Done stage."))

    @api.depends('user_ids')
    def _compute_department_id(self):
        for rec in self:
            rec.department_id = False
            rec.direct_manager_id = False
            if rec.user_ids:
                for user_id in rec.user_ids:
                    if user_id.employee_id:
                        if user_id.employee_id.department_id:
                            rec.department_id = user_id.employee_id.department_id.id
                        if user_id.employee_id.parent_id and user_id.employee_id.parent_id.user_id:
                            rec.direct_manager_id = user_id.employee_id.parent_id.user_id.id

    # @api.depends('direct_manager_id')
    # def _compute_is_direct_manager(self):
    #     for rec in self:
    #         if self.env.user.id == rec.direct_manager_id.id:
    #             rec.is_direct_manager = True
    #         else:
    #             rec.is_direct_manager = False

    @api.depends('stage_id', 'direct_manager_id')
    def _compute_is_assessments_readonly(self):
        for rec in self:
            if rec.stage_id.name == "Done" and self.env.user.has_group('hr.group_hr_manager'):
                rec.is_assessments_readonly = False
            elif rec.stage_id.name != "Done" and self.env.user.id == rec.direct_manager_id.id:
                rec.is_assessments_readonly = False
            elif rec.stage_id.name != "Done" and self.env.user.has_group('base.group_system'):
                rec.is_assessments_readonly = False
            else:
                rec.is_assessments_readonly = True

    def _set_department_for_tasks_cron(self):
        all_tasks = self.env['project.task'].search([])
        for rec in all_tasks:
            rec.department_id = False
            if rec.user_ids:
                for user_id in rec.user_ids:
                    if user_id.employee_id:
                        if user_id.employee_id.department_id:
                            rec.department_id = user_id.employee_id.department_id.id
                        if user_id.employee_id.parent_id:
                            rec.requested_by = user_id.employee_id.parent_id.user_id.id
