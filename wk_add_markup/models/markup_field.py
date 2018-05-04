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

    markup = fields.Float(string="Mark up(%)")

    @api.multi
    @api.onchange('product_id','markup')
    def change_product_markup(self):
        if self.product_id:
            self.markup = self.product_id.markup
            self.price_unit = self.product_id.standard_price*(1 + self.markup/100)


class ProductTemplate(models.Model):
    
    _inherit = "product.template"

    markup = fields.Float(string="Mark up (%)")