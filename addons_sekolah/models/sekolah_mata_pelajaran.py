from odoo import models, fields

class MataPelajaran(models.Model):
    _name = 'sekolah.mata_pelajaran'
    _description = 'Mata Pelajaran'

    name = fields.Char(string='Name')