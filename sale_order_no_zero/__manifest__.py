# -*- coding: utf-8 -*-
{
    'name': "Sale Order: No Zero Quantity",

    'summary': 'Prevent confirming sale orders with zero quantity lines and add button to delete them',

    'description': """
This module prevents confirming sale orders that have lines with quantity zero.
It also adds a button to delete only the lines with quantity zero from the order.
""",

    'author': "Binovo",
    'website': "https://www.yourcompany.com",

    # Category
    'category': 'Website',
    'version': '18.0.1.0.2',

    # Modules required for this module to work
    'depends': ['sale'],

    # Always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',    
    ],

    # Only loaded in demonstration mode (optional)
    'demo': [
        # 'demo/demo.xml',
    ],

    'installable': True,
    'application': False,
}
