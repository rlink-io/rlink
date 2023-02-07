# -*- coding: utf-8 -*-
# from odoo import http


# class RlinkProjectEdits(http.Controller):
#     @http.route('/rlink__project__edits/rlink__project__edits/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rlink__project__edits/rlink__project__edits/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rlink__project__edits.listing', {
#             'root': '/rlink__project__edits/rlink__project__edits',
#             'objects': http.request.env['rlink__project__edits.rlink__project__edits'].search([]),
#         })

#     @http.route('/rlink__project__edits/rlink__project__edits/objects/<model("rlink__project__edits.rlink__project__edits"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rlink__project__edits.object', {
#             'object': obj
#         })
