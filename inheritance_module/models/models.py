# -*- coding: utf-8 -*-

from odoo import models, fields, api


class inheritance_module(models.Model):
    # _name = 'inheritance_module.inheritance_module'
    _inherit = 'test_module.test_module'
    name = fields.Char()
    description = fields.Text()
    root_value = fields.Integer()
    inhertance_value = fields.Integer(compute="_value_inheritance", store=True)

    @api.depends('value')
    def _value_inheritance(self):
        self.inhertance_value = self.value * 2