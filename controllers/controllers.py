# -*- coding: utf-8 -*-
# from odoo import http


# class ReinosDeFuego(http.Controller):
#     @http.route('/reinos_de_fuego/reinos_de_fuego', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reinos_de_fuego/reinos_de_fuego/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('reinos_de_fuego.listing', {
#             'root': '/reinos_de_fuego/reinos_de_fuego',
#             'objects': http.request.env['reinos_de_fuego.reinos_de_fuego'].search([]),
#         })

#     @http.route('/reinos_de_fuego/reinos_de_fuego/objects/<model("reinos_de_fuego.reinos_de_fuego"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reinos_de_fuego.object', {
#             'object': obj
#         })

