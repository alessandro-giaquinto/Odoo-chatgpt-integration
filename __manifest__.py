{
    'name': 'Odoo ChatGpt Custom Integration',
    'version': '1.0',
    'category': 'website',
    'summary': 'An odoo module that use ChatGpt integration for re-arrange a text',
    'description': 'This module provide custom chatGpt integration for Odoo 17.',
    'license': 'LGPL-3',
    'author': 'Alten',
    'depends': ['base', 'base_setup', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/main_view.xml',
    ],
    'installable': True,
    'application': True,
} 