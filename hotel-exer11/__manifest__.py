# -*- coding: utf-8 -*-
{
    'name': "Hotel Management System",
    'summary': "Hotel Management System",
    'description': "Hotel Management System",
    'author': "Aki",


    'category': 'Uncategorized',
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/mainmenu.xml',
        'views/charges.xml',
        'views/roomtypes.xml',
        'views/rooms.xml',
        'views/guests.xml',
    ],
    'installable': True,
    'application': True,
}