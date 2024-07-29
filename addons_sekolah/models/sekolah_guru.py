from odoo import models, fields

class Guru(models.Model):
    _name = 'sekolah.guru'
    _description = 'Guru'

    name = fields.Char(string='Name')
    mapel_id = fields.Many2one('sekolah.mata_pelajaran', string='Mata Pelajaran')