from odoo import models, fields,api

class AccountMove(models.Model):
    _inherit = 'account.move'

    delivery_charge = fields.Float(string='Delivery Charge')
