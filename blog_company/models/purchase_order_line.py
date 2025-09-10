from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order.line'

    secondary_unit = fields.Many2one('uom.uom', string='2nd Unit')
    calculation_factor = fields.Float('Calculation Factor')

    @api.onchange('price_unit')
    def _onchange_price_unit(self):
        """When the unit price changes, the factor is recalculated"""
        # self.product_id returns an empty product, so it
        # is taken from the order_id
        # Takes product_id from order or self.product_id
        product_id = self.order_id.product_id or self.product_id
        # If theres not calculation factors means is recently added to
        # order and need this values
        if not self.calculation_factor:
            self.calculation_factor = product_id.calculation_factor
            self.secondary_unit = product_id.secondary_unit
        else:  # Else has been manually updated
            if self.price_unit and product_id.lst_price:
                # lst_price is a base price of the product is in order_id
                self.calculation_factor = self.price_unit / product_id.lst_price
            else:
                self.calculation_factor = 0.0

    @api.onchange('calculation_factor')
    def _onchange_calculation_factor(self):
        """When the calculation factor changes, the unit price is recalculated"""
        product_id = self.order_id.product_id
        if self.secondary_unit:
            if self.calculation_factor and product_id.lst_price:
                self.price_unit = self.calculation_factor * product_id.lst_price

    @api.model
    def _prepare_account_move_line(self, move=False):
        res = super()._prepare_account_move_line(move)
        res['calculation_factor'] = self.calculation_factor
        return res
