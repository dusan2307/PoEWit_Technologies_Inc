# -*- coding: utf-8 -*-
{
    'name': 'PoEWit Technologies Inc: Adding a sound file & changing attachment icon on website',
    'summary': 'Customization on the web (sound,download button)',
    'sequence': 100,
    'license': 'OPL-1',
    'website': 'https://www.odoo.com',
    'version': '1.2',
    'author': 'Odoo Inc',
    'description': """
    -  2286978
    """,
    'category': 'Custom Development',

    # any module necessary for this one to work correctly
    'depends': ['website_sale', 'website_sale_wishlist'],

    # always loaded
    'data': [
        'views/poewit_web_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'poewit_web/static/src/scss/style.scss',
            'poewit_web/static/src/js/play_audio.js',
        ],
    },
    'installable': True,
    'auto_install': False,
}