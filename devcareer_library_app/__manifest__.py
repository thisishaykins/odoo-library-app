{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'A Simple library management system',
    'description': """
       Manage books, loans, etc
    """,
    'category': 'Management,Books',
    "author": "Akinshola Samuel",
    "license": 'LGPL-3',
    "website": "akinshola.com",
    'depends': ['base', 'hr', 'contacts', 'mail',],
    'data': [
        'security/security.xml',
        'views/views.xml',
        'views/actions.xml',
        'menus/menus.xml',
        'data/data.xml',
    ],
    'icon': '/devcareer_library_app/static/description/icon.png',
    'images': [
        '/devcareer_library_app/static/description/icon.png',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
