from odoo import models
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    # Bloquear confirmación si hay líneas con cantidad 0
    def action_confirm(self):
        for order in self:
            zero_lines = order.order_line.filtered(lambda l: l.product_uom_qty <= 0)
            if zero_lines:
                raise UserError("Cannot confirm the sale order: there are lines with quantity 0.")
        return super().action_confirm()

    # Botón para eliminar líneas con cantidad 0
    def delete_zero_lines(self):
        for order in self:
            zero_lines = order.order_line.filtered(lambda l: l.product_uom_qty <= 0)
            zero_lines.unlink()
