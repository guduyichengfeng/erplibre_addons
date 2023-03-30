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
        # aliments = request.env['aliment.aliments'].search([])
        # names = [a.name for a in aliments]
        # return {"listes_aliments": names}
        aliments = request.env['aliment.aliments'].search([])
        data = [{'id': a.id, 'name': a.name} for a in aliments]  # include the ID of each aliment
        return {"listes_aliments": data}

    @http.route(
        '/creer',
        type="json",
        auth="public",
        website=True,
    )
    def ajouterAliment(self, **post):
        http.request.env['aliment.aliments'].sudo().create({'name': post.get('name')})

    @http.route(
        '/modifier',
        type="json",
        auth="public",
        website=True,
    )
    def modifierAliment(self, **post):
        aliment_id = post.get('aliment_id')
        aliment = request.env['aliment.aliments'].sudo().browse(int(float(aliment_id)))
        aliment.write({'name': post.get('name')})
        return self.afficher_liste()

