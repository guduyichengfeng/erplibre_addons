from odoo import http
from odoo.http import request

#
# class AlimentController(http.Controller):
#     @http.route(
#         ["/aliment/liste"],
#         type="json",
#         auth="public",
#         website=True,
#         methods=["POST", "GET"],
#         csrf=False,
#     )
#     def list_aliments(self, **kw):
#         return http.request.render('aliment.list_aliment', {
#             'aliments': ["Viandes", "Légumes", "Fruits"],
#         })

# @http.route('/aliments', auth='public', website=True)
# def aliments(self, **kw):
#     aliments = ['Apple', 'Banana', 'Cherry']
#     return http.request.render('aliment.s_aliment', {'aliments': aliments})
class AlimentController(http.Controller):
    @http.route(
        ["/aliment/liste"],
        type="json",
        auth="public",
        website=True,
        methods=["POST", "GET"],
        csrf=False,
    )
    def afficher_liste(self):
        return {"aliment": ["Viandes", "Légumes", "Fruits"]}



