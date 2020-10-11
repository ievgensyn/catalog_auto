{
    'name': 'Catalog auto',
    'version': '13.0.0.0.4',
    'license': 'Other proprietary',
    'category': 'Technical Settings',

    'summary': 'Extend product management',

    'complexity': 'easy',
    'sequence': 3,

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'depends': [
        'stock', 'product_brand_inventory',
    ],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/catalog_auto_view.xml',
        'views/product_brand_view.xml',
        'views/product_template_view.xml',
        'views/menu_items.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
