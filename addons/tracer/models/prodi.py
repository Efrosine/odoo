# -*- coding: utf-8 -*-

from odoo import models, fields, api

class prodi(models.Model):
     _name = 'tracer.prodi'
     _description = 'Menyimpan Data Prodi'

     name = fields.Char()
     description = fields.Text()

   