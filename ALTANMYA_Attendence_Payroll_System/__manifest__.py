# -*- coding: utf-8 -*-
###################################################################################
#
#    ALTANMYA - TECHNOLOGY SOLUTIONS
#    Copyright (C) 2022-TODAY ALTANMYA - TECHNOLOGY SOLUTIONS Part of ALTANMYA GROUP.
#    ALTANMYA Attendance Device Adaptor.
#    Author: ALTANMYA for Technology(<https://tech.altanmya.net>)
#
#    This program is Licensed software: you can not modify
#   #
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################
{
    'name': 'ALTANMYA Attendance Device Adaptor',
    'version': '1.0',
    'summary': 'This ALTANMYA module integrates Odoo attendance with attendance devices (Suprema and Zk)',
    'description': "End to End process for Attendance Process with devices",
    'category': 'Human Resources/Employees',
    'author': 'ALTANMYA - TECHNOLOGY SOLUTIONS',
    'company': 'ALTANMYA - TECHNOLOGY SOLUTIONS Part of ALTANMYA GROUP',
    'website': "https://tech.altanmya.net",
    'depends': ['hr','resource','hr_attendance','hr_contract','hr_payroll', 'mail','contacts'],
    'data': ['views/view_v.xml',
             'security/ir.model.access.csv',
             'security/security.xml',
             'views/cron_jobs.xml',
             'views/tstyle.xml',
             'views/view_actions.xml',
             'views/view_menu.xml',
             'data/data.xml',
             'data/custom_channels.xml',
             'views/employee.xml',
             'views/hr_contract_inherited.xml',
             'views/employee_top_row_views.xml',
             'views/change_request.xml',

             ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {
    'web.assets_backend': [
    '/ALTANMYA_Attendence_Payroll_System/static/src/css/style.css',
    ]},

}
