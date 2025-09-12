# -*- coding: utf-8 -*-
{
    'name': "CRM Lead Custom",

    'summary': "Customizations for CRM leads and website contact form",

    'description': """
Customizes CRM Leads and Website Contact form:
- Adds 'Source Type' field in CRM.
- Updates website contact form (remove phone, company optional, source required, email validation).
""",

    'author': "Binovo",
    'website': "https://www.yourcompany.com",

    # Category
    'category': 'Website',
    'version': '18.0.1.0.1',

    # Modules required for this module to work
    'depends': ["crm", "website_crm"],

    # Always loaded
    'data': [
        'security/ir.model.access.csv',
        "views/website_crm_form.xml",
    ],

    # Only loaded in demonstration mode (optional)
    'demo': [
        # 'demo/demo.xml',
    ],

    'installable': True,
    'application': False,
}
