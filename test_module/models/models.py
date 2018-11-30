# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course1(models.Model):
    _name = 'test_module.course'
    _description = "test_module.course description"

    description = fields.Text()
    name = fields.Text()


class Session1(models.Model):
    _name = 'test_module.session'
    _description = "OpenAcademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    # course_id = fields.Many2one('test_module.course',ondelete='cascade', string="Course", required=True)
    test_module_id = fields.Many2one("test_module.test_module", string="Test Module")
    course_ids = fields.Many2many('test_module.course', string="Attendee")


class test_module(models.Model):
    _name = 'test_module.test_module'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many('test_module.session', 'test_module_id', string="Sessions")

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100

    def test(self):
        return "test"