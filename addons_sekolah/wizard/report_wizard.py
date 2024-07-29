from odoo import models, fields, api

class SiswaReportWizard(models.TransientModel):
    _name = 'sekolah.report.wizard'
    _description = 'Wizard for generating Siswa report'

    def get_report(self):
        """Call when button 'Get Report' clicked.
        """
        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
            },
        }
        return self.env.ref('addons_sekolah.recap_report').report_action(self, data=data)

class ReportSiswa(models.AbstractModel):
    _name = 'report.addons_sekolah.siswa_report_view'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = []
        siswas = self.env['sekolah.siswa'].search([], order='name asc')
        for siswa in siswas:
            
            docs.append({
                'siswa': siswa.name,
                'date_of_birth': siswa.date_of_birth,
                'kelas': siswa.kelas_id.name,
                'guru': siswa.guru_id.name,
                'mata_pelajaran': siswa.mata_pelajaran_id.name,
            })

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'docs': docs,
        }