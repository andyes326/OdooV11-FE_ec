# -*- coding: utf-8 -*-
{
    'name': "Account user custom formats",
    'summary': """Users can use their own format definitions.""",
    'version': '9.0.1.0.1',
    'author': "Fabrica de Software Libre",
    'maintainer': 'Fabrica de Software Libre',
    'website': 'http://www.fslibre.com',
    'license': 'AGPL-3',
    'category': 'Account',
    'depends': [
        'base',
        'account',
        'base_report_custom_format',
        'l10n_ec_payment',
    ],
    'data': [
        'views/res_users.xml',
        'views/report_account_payment.xml',
        'views/report_account_move.xml',
        'views/account.xml',
        'views/account_payment.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
