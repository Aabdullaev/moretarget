# -*- coding: utf-8 -*-

from odoo import models, fields, api, addons
import logging


class inheritance_module(models.Model):
    # _name = 'inheritance_module.inheritance_module'
    _inherit = 'test_module.test_module'
    name = fields.Char()
    description = fields.Text()
    root_value = fields.Integer()
    inhertance_value = fields.Integer()
    product_ids = fields.Many2one("product.template", string="Product")

    # @api.depends('root_value')
    # def _value_inheritance(self):
    #     logging.info(self.test())
    #     self.value = self.root_value * 2

    def test(self):
        return "Test Inheritance"

    @api.onchange('value', 'root_value')
    def _onchange_value(self):
        self.inhertance_value = self.value + self.root_value
        return {
            'warning': {
                'title': "Something bad happened",
                'message': "It was very bad indeed",
            }
        }

    @api.constrains('root_value')
    def _check_something(self):
        for record in self:
            if record.root_value == 0:
                logging.info("_check_something error");