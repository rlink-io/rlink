from odoo import api, models, fields, _


class ReportProjectTaskUserInherited(models.Model):
    _inherit = "report.project.task.user"
    department_id = fields.Many2one('hr.department', readonly=True, string="Department")

    def _select(self):
        return super()._select() + ", t.department_id"

    def _group_by(self):
        return super()._group_by() + ", t.department_id"

