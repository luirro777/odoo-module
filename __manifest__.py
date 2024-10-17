# -*- coding: utf-8 -*-
{
    'name': "Modulo de ejemplo",

    'summary':"""
        Ejemplo agregado con submodules""",

    'description': """
        El proposito es mostrar cómo proceder a la hora de 
        desarrollar modulos con un entorno basado en el uso
        de docker-compose.
        Actualizacion de modulo
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
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
