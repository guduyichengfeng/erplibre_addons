from odoo import _, api, fields, models


class AlimentInternal(models.Model):
    _name = "aliment.internal"
    _inherit = ["mail.activity.mixin", "mail.thread"]
    _description = "aliment_internal"

    name = fields.Char()

    # Banana demo
    aliment = fields.Boolean(string="Aliment")

    date_end = fields.Datetime(string="Date end")

    date_start = fields.Datetime(string="Date start")

    empty = fields.Text()
    # End of DemoModelInternal
