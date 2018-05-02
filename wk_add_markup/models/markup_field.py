# -*- coding: utf-8 -*-
##########################################################################
#
#    Copyright (c) 2017-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#
##########################################################################

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class SaleOrderLine(models.Model):

    _inherit = "sale.order.line"

    markup = fields.Float(string="Mark up (In percetage)")

    @api.multi
    @api.onchange('product_id','markup')
    def change_product_markup(self):
        if self.product_id and self.markup:
            self.price_unit = self.product_id.standard_price*(1 + self.markup/100)