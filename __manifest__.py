# -*- coding: utf-8 -*-
{
    'name': "musicEvents",

    'summary': """
        The module description is for the management of music events.""",

    'description': """
        The purpose of the module is to manage the music events of the company app.
    """,

    'author': "Music Events",
    'website': "http://www.musicevents.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}