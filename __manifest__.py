{
    'name': 'Odoo ChatGpt Integration',
    'summary': 'An odoo module that use ChatGpt integration for re-arrange a text',
    'description': 'This module provide custom chatGpt integration for Odoo 17.',
    'category': 'website',# vedi su https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml per una lista completa
    'version': '0.1',
    'license': 'LGPL-3',
    'author': 'Alessandro Giaquinto @ Alten',
    'depends': ['base', 'web'],
    'installable': True,
    'application': True,
    'data': [
        'views/templates.xml',# Odoo caricherà solo questa view, il resto viene gestito dal framework OWL (tutto quello che è presente in static/src)
    ],
    'assets': {
        'oci.assets': [# oci = Odoo ChatGPT Integration, usato come abbreviativo, se modificato allora modifica anche la relativa parte nel templates.xml
            # Copiato completamente dal repo di cui sopra
            # bootstrap
            ('include', 'web._assets_helpers'),
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            ('include', 'web._assets_bootstrap_backend'),
            
            # include base files from framework
            ('include', 'web._assets_core'),

            # remove some files that we do not use to create a minimal bundle
            ('remove', 'web/static/src/core/**/*'),
            ('remove', 'web/static/lib/luxon/luxon.js'),
            'web/static/src/core/utils/concurrency.js',
            'web/static/src/core/utils/strings.js',
            'web/static/src/core/l10n/translation.js',
            'web/static/src/core/utils/functions.js',
            'web/static/src/core/browser/browser.js',
            'web/static/src/core/registry.js',
            'web/static/src/core/assets.js',
        ]
    },
} 