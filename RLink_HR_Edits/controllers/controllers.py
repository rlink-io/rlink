# -*- coding: utf-8 -*-
# from odoo import http


# class RLinkHrEdits(http.Controller):
#     @http.route('/r__link__hr__edits/r__link__hr__edits/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/r__link__hr__edits/r__link__hr__edits/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('r__link__hr__edits.listing', {
#             'root': '/r__link__hr__edits/r__link__hr__edits',
#             'objects': http.request.env['r__link__hr__edits.r__link__hr__edits'].search([]),
#         })

#     @http.route('/r__link__hr__edits/r__link__hr__edits/objects/<model("r__link__hr__edits.r__link__hr__edits"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('r__link__hr__edits.object', {
#             'object': obj
#         })
