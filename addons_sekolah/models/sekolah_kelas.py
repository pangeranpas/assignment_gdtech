from odoo import models, fields

class Kelas(models.Model):
    _name = 'sekolah.kelas'
    _description = 'Kelas'

    name = fields.Char(string='Name')