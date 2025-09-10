# -*- coding: utf-8 -*-
{
    'name': "blog_company",

    'summary': "Associate blogs and posts to a company",

    'description': """
Allows associating a blog to a company and inherits the company in the blog posts.
Users can only view and manage blogs and posts of their company and its child companies.
    """,

    'author': "Binovo",
    'website': "https://www.yourcompany.com",

    # Category
    'category': 'Website',
    'version': '18.0.1.0.0',

    # Modules required for this module to work
    'depends': ['website_blog'],

    # Always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/blog_security.xml',
        'views/blog_views.xml',    
    ],

    # Only loaded in demonstration mode (optional)
    'demo': [
        # 'demo/demo.xml',
    ],

    'installable': True,
    'application': False,
}
