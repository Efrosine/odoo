# -*- coding: utf-8 -*-
# from odoo import http


# class Pajar(http.Controller):
#     @http.route('/pajar/pajar', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pajar/pajar/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pajar.listing', {
#             'root': '/pajar/pajar',
#             'objects': http.request.env['pajar.pajar'].search([]),
#         })

#     @http.route('/pajar/pajar/objects/<model("pajar.pajar"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pajar.object', {
#             'object': obj
#         })

