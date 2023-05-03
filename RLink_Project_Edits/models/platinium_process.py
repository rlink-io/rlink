from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError


class SaleOrderInherited(models.Model):
    _inherit = 'sale.order'

    def confirm_order(self):
        self.action_confirm()
        return 'Confirm'
