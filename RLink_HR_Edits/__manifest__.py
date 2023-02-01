# -*- coding: utf-8 -*-
{
    'name': "R-Link HR Edits",

    'summary': """
        """,

    'description': """
       
    """,

    'author': "Momena Sukkar",
    'Email': "momenasukkar@gmail.com",
    'LinkedIn Profile': "https://www.linkedin.com/in/momena-sukkar-457692210",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','hr_contract','hr_payroll', 'mail', 'contacts', 'hr_holidays'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/cron_jobs.xml',
        'views/employee.xml',
        'views/hr_contract_inherited.xml',
        'views/employee_top_row_views.xml',
        'views/change_request.xml',
        'views/hr_payslip_inherited.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            '/RLink_HR_Edits/static/src/css/style.css',
        ]},
}
