from odoo import models, fields, api

class Aliments(models.Model):
    _name = 'aliment.aliments'
    _description = 'Aliments'

    name = fields.Char()

    id = fields.Id()
