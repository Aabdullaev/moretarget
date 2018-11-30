# -*- coding: utf-8 -*-
from odoo import http

# class InheritanceModule(http.Controller):
#     @http.route('/inheritance_module/inheritance_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inheritance_module/inheritance_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inheritance_module.listing', {
#             'root': '/inheritance_module/inheritance_module',
#             'objects': http.request.env['inheritance_module.inheritance_module'].search([]),
#         })

#     @http.route('/inheritance_module/inheritance_module/objects/<model("inheritance_module.inheritance_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inheritance_module.object', {
#             'object': obj
#         })