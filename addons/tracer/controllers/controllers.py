# -*- coding: utf-8 -*-
# from odoo import http


# class tracer(http.Controller):
#     @http.route('/tracer/tracer', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tracer/tracer/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tracer.listing', {
#             'root': '/tracer/tracer',
#             'objects': http.request.env['tracer.tracer'].search([]),
#         })

#     @http.route('/tracer/tracer/objects/<model("tracer.tracer"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tracer.object', {
#             'object': obj
#         })

