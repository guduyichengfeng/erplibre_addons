from odoo import _, api, fields, models


class Aliment2Internal(models.Model):
    _name = "aliment_2.internal"
    _description = "aliment_2_internal"

    name = fields.Char()

    # Model_2 contain model_1
    # Only 1 time
    model_1 = fields.Many2one(comodel_name="aliment.internal")
