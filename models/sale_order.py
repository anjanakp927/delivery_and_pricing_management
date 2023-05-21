
from odoo import models, fields,api
from odoo.exceptions import ValidationError



class SaleOrder(models.Model):
    _inherit = 'sale.order'

    delivery_charge = fields.Monetary(string='Delivery Charge', compute='_compute_delivery_charge', store=True)

    @api.depends('amount_total')
    def _compute_delivery_charge(self):
        for order in self:
            order.delivery_charge = order.amount_total * 0.1

    @api.depends('order_line.price_total', 'delivery_charge', 'currency_id', 'company_id', 'date_order')
    def _amount_all(self):
        for order in self:
            super(SaleOrder, order)._amount_all()
            order.amount_total += order.delivery_charge

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['delivery_charge'] = self.delivery_charge
        return invoice_vals

    def _create_invoices(self, grouped=False, final=False):
        res = super(SaleOrder, self)._create_invoices(grouped=grouped, final=final)
        for order in self:
            for invoice in order.invoice_ids:
                invoice.amount_total = order.amount_total
        return res

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    brand_name = fields.Char(string='Brand Name', related='product_id.brand_name')

    @api.model
    def create(self, values):
        if 'product_id' in values and 'price_unit' in values:
            product = self.env['product.template'].browse(values['product_id'])
            if values['price_unit'] < product.minimum_cost:
                raise ValidationError("Unit price cannot be less than the minimum cost of the product.")
        return super(SaleOrderLine, self).create(values)
