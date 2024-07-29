from odoo import models, fields, api

class SiswaReportWizard(models.TransientModel):
    _name = 'sekolah.report.wizard'
    _description = 'Wizard for generating Siswa report'

    def generate_report(self):
        """Call when button 'Get Report' clicked.
        """

        sort = "id"
      
        domain = []
        
        lines = self.env['sekolah.siswa'].search(domain,order=sort)

        docs = []
        
        for line in lines:

            docs.append({
                'name': line.name or False,
            })
                
        data = {
            'doc_ids': self.ids,
            'doc_model': self._name,
            'docs': docs,
        }
        
        # use `module_name.report_id` as reference.
        # `report_action()` will call `get_report_values()` and pass `data` automatically.
        return self.env.ref('addons_sekolah.custom_report_action').report_action(self, data=data)
    
    # def generate_report(self):
    #     # Fetch all student records
    #     students = self.env['sekolah.siswa'].search([])
    #     data = {
    #         'doc_ids': students.ids,
    #         'doc_model': 'sekolah.siswa',
    #         'docs': students,
    #     }
    #     return self.env.ref('addons_sekolah.custom_report_action').report_action(self, data=data)

class ReportExampleWizard(models.AbstractModel):
    """Abstract Model for report template.
    for `_name` model, please use `report.` as prefix then add `module_name.report_name`.
    """

    _name = 'report.addons_sekolah.custom_report_template'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['sekolah.siswa'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'sekolah.siswa',
            'docs': docs,
        }