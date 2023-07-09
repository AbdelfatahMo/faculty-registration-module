# -*- coding: utf-8 -*-
{
    'name': "Faculty Registration",

    'summary': "Control the process of registrations",

    'description': "Control the process of registrations and save student information",

    'author': "Obadoo",
    'website': "abdelfatah_mohamed@w-ist.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Registration/Faculty',
    'version': '15.0',
    'license': 'AGPL-3',
    'sequence': '-10',
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/application.xml',
        'views/family.xml',
        'views/faculty.xml',
        'views/skill.xml',
        'views/menus.xml',
    ],
    
    'application': True,
    'installable': True,
    'auto_install': False,
}
