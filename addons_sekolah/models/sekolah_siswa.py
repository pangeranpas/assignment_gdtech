from odoo import models, fields

class Siswa(models.Model):
    _name = 'sekolah.siswa'
    _description = 'Siswa'

    name = fields.Char(string='Name')
    date_of_birth = fields.Date(string='Date of Birth')
    kelas_id = fields.Many2one('sekolah.kelas', string='Kelas')
    guru_id = fields.Many2one('sekolah.guru', string='Guru')
    mata_pelajaran_id = fields.Many2one(related='guru_id.mapel_id', string='Mata Pelajaran', store=True)