# -*- coding: utf-8 -*-
{
    'name': "Addons untuk Sekolah",

    'summary': """
        Modul Sekolah""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Pangeran Chrisitan",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sekolah_siswa_views.xml',
        'views/sekolah_kelas_views.xml',
        'views/sekolah_guru_views.xml',
        'views/sekolah_mata_pelajaran_views.xml',
        'views/menuitem.xml',
        'reports/sekolah_report_templates.xml',
        'wizard/sekolah_report_wizard.xml',
    ],
}
