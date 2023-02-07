from odoo import api, models, fields, _


class UsersManagement(models.Model):
    _name = "project.users.management"
    _description = "Project Users Management"

    display_name = fields.Char(default='Timesheet Document Logging Upload')

    optional_users = fields.Many2many('res.users')
