# -*- coding: utf-8 -*-
{
    'name': 'PoEWit Technologies Inc: Adding a sound file & changing attachment icon on website',
    'summary': 'Customization on the web (sound,download button)',
    'sequence': 100,
    'license': 'OEEL-1',
    'website': 'https://www.odoo.com',
    'version': '1.1',
    'author': 'Odoo Inc',
    'description': """
    -  2286978
    """,
    'category': 'Custom Development',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        'views/poewit_web_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}