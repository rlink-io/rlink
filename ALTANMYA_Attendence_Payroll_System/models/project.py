from odoo import api, models, fields, _
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError
from bs4 import BeautifulSoup


class ProjectInherited(models.Model):
    _inherit = 'project.project'

    @api.model
    def create(self, vals):
        rec = super(ProjectInherited, self).create(vals)

        to_do = self.env['project.task.type'].create({'name': 'To Do', 'sequence': 1})

        doing = self.env['project.task.type'].create({'name': 'Doing', 'sequence': 2})

        to_check = self.env['project.task.type'].create({'name': 'To Check', 'sequence': 3})

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
    total = fields.Float(string='Total')
    task_number = fields.Integer(string='task.No')
    requested_by = fields.Many2one('res.users',
                                   string="Requested By")
    department_id = fields.Many2one('hr.department', compute="_compute_department_id", store=True)
    description = fields.Html(required=True)
    planned_date_from = fields.Date("Start date ")
    planned_date_to = fields.Date("End date ")

    planned_date_begin = fields.Datetime("Start date", tracking=True, task_dependency_tracking=True,
                                         compute="_compute_planned_date_begin")
    planned_date_end = fields.Datetime("End date", compute="_compute_planned_date_end")
    direct_manager_id = fields.Many2one('res.users', compute="_compute_department_id", store=True)
    is_direct_manager = fields.Boolean(compute="_compute_is_direct_manager")
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
                if len(timesheet.name) < 25:
                    raise ValidationError(
                        "The Description of timesheet line cannot be empty and should be more than 25 characters.")
                optional_users_ids = self.env['project.users.management'].search([('id', '=', 1)]).optional_users.ids
                if timesheet.employee_id.user_id.id not in optional_users_ids and timesheet.document_attachment == False:
                    raise ValidationError(
                        "The Document in timesheet line is required.")

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
        rec = super(ProjectTaskInherited, self).create(vals_list)
        if 'user_ids' in vals_list and not 'requested_by' in vals_list:
            for user_id in rec.user_ids:
                if user_id.employee_id:
                    if user_id.employee_id.parent_id:
                        rec.requested_by = user_id.employee_id.parent_id.user_id.id
                        break
        return rec

    def check_stage_restrictions(self, vals):
        if self.stage_id.name == 'Done' and not self.env.user.has_group('hr.group_hr_manager'):
            raise UserError(
                _("You are not allowed to change the stage of task please contact with the HR manager!"))
        if self.stage_id.name == 'To Check':
            new_stage = self.env['project.task.type'].search([('id', '=', vals['stage_id'])])
            if new_stage.name == "Done":
                if self.env.user.id != self.direct_manager_id.id:
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

    @api.depends('direct_manager_id')
    def _compute_is_direct_manager(self):
        for rec in self:
            if self.env.user.id == rec.direct_manager_id.id:
                rec.is_direct_manager = True
            else:
                rec.is_direct_manager = False

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


class account_analytic_line_inherited(models.Model):
    _inherit = 'account.analytic.line'

    document_attachment = fields.Binary(string="Document")


class ReportProjectTaskUserInherited(models.Model):
    _inherit = "report.project.task.user"
    department_id = fields.Many2one('hr.department', readonly=True, string="Department")

    def _select(self):
        return super()._select() + ", t.department_id"

    def _group_by(self):
        return super()._group_by() + ", t.department_id"


class UsersManagement(models.Model):
    _name = "project.users.management"
    _description = "Project Users Management"

    display_name = fields.Char(default='Timesheet Document Logging Upload')

    optional_users = fields.Many2many('res.users')


class mail_message_inherited(models.Model):
    _inherit = 'mail.message'

    note = fields.Html(string='Note')

    @api.model
    def create(self, vals_list):
        rec = super(mail_message_inherited, self).create(vals_list)
        if rec.model == 'project.task':
            if rec.subtype_id.name != 'Discussions':
                self.get_message_note(rec)
            task_id = self.env['project.task'].search([('id', '=', int(rec.res_id))])
            for user in task_id.message_partner_ids:
                if user.id != rec.author_id.id:

                    channel = self.env['mail.channel'].channel_get(
                        [user.id])
                    channel_id = self.env['mail.channel'].browse(channel["id"])
                    if rec.subtype_id.name == 'Discussions':
                        body = ('{author} sent a message In {name} Task chatter with content: {message} '.format(
                            author=rec.author_id.name,
                            name=task_id.name,
                            message=rec.body,
                            message_type='comment',
                            subtype_xmlid='mail.mt_comment'))
                    else:
                        body = ('{author} wrote a note In {name} Task chatter with content: {note} '.format(
                            author=rec.author_id.name,
                            name=task_id.name,
                            note=rec.note,
                            message_type='comment',
                            subtype_xmlid='mail.mt_comment'))

                    channel_id.message_post(body=body)
        return rec

    def get_message_note(self, message):
        if message.body:
            message.note = message.body
        else:
            message.note = (
                    """<div><p>""" + message.subtype_id.description + """</p></div>""") if message.subtype_id.description else """"""
            if message.sudo().tracking_value_ids:
                for value in message.tracking_value_ids:
                    message.note = """<div>""" + str(message.note) + """</div><span>""" + str(
                        value.field_desc) + """<span>:  </span> </span>"""
                    if value.field_type == 'datetime':
                        message.note = str(message.note) + """<span>""" + str(
                            value.old_value_datetime) + """</span><span>  =>  """ + str(
                            value.new_value_datetime) + """</span>"""
                    elif value.field_type == "float":
                        message.note = str(message.note) + """<span>""" + str(
                            value.old_value_float) + """</span><span>  =>  """ + str(
                            value.new_value_float) + + """</span>"""
                    elif value.field_type == "integer":
                        message.note = str(message.note) + """<span>""" + str(
                            value.old_value_integer) + """</span><span>  =>  """ + str(
                            value.new_value_integer) + """</span>"""
                    else:
                        message.note = str(message.note) + """<span>""" + str(
                            value.old_value_char) + """</span><span>  =>  """ + str(
                            value.new_value_char) + """</span>"""
        return message.note
