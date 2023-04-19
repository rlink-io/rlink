# -*- coding: utf-8 -*-
{
     'name': "R-Link Project Edits",

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
    'depends': ['base', 'ALTANMYA_Attendence_Payroll_System', 'project', 'project_enterprise', 'hr_timesheet',
                'timesheet_grid'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/cron_jobs.xml',
        'views/project_task_view_inherited.xml',
        'views/project_user_management_view.xml',
        'views/report_project_task_user_view.xml',
        'views/employee_project_reports.xml',
        'views/project_dynamic_tasks_report.xml',
        'views/project_timesheet_report_view.xml'
    ],
    # only loaded in demonstration mode

    'installable': True,
    'auto_install': False,
    'application': True,
}
