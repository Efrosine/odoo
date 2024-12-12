from odoo import models, fields


class agama(models.Model):
    _name = 'pajar.agama'
    _description = 'pajar.agama'

    name = fields.Char()
    description = fields.Text()