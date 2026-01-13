# -*- coding: utf-8 -*-
# from odoo import http


# class SmvInstituto(http.Controller):
#     @http.route('/smv_instituto/smv_instituto', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/smv_instituto/smv_instituto/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('smv_instituto.listing', {
#             'root': '/smv_instituto/smv_instituto',
#             'objects': http.request.env['smv_instituto.smv_instituto'].search([]),
#         })

#     @http.route('/smv_instituto/smv_instituto/objects/<model("smv_instituto.smv_instituto"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('smv_instituto.object', {
#             'object': obj
#         })

