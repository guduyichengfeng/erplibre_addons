from odoo import models, fields, api

class Aliments(models.Model):
    _name = 'aliment.aliments'
    _description = 'Aliments'

    name = fields.Char()

    pomme = fields.Boolean(string="Pomme demo")

    date_end = fields.Datetime(string="Date end")

    date_start = fields.Datetime(string="Date start")

    empty = fields.Text()
