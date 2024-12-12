# models/fakultas.py
from odoo import models, fields

class fakultas(models.Model):
    _name = 'tracer.fakultas'
    _description = 'Data Fakultas'

    name = fields.Char(string='Nama Fakultas', required=True)
