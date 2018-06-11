# -*- coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Account check deposit date',
    'version': '9.0.1.0.0',
    'category': 'Accounting',
    'sequence': 14,
    'summary': '',
    'author': 'FÁBRICA DE SOFTWARE LIBRE',
    'website': 'www.fslibre.com',
    'license': 'AGPL-3',
    'images': [
    ],
    'depends': [
        'account',
        'account_check_deposit',
    ],
    'data': [
        'views/account_move.xml',
        'views/account_payment.xml',
        'views/check_deposit.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
