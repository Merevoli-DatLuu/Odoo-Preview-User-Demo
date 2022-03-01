{ 
    'name': "User Preview",
    'summary': "Show preview page to view information of a user in the system",
    'description': """ 
        User Preview
        ==============
        Description related to module.
    """, 
    'sequence': 10,
    'author': "Your name", 
    'website': "http://www.example.com", 
    'category': 'Uncategorized', 
    'version': '13.0.1', 
    'depends': ['base'], 
    'data': [
        'security/groups.xml',
        'views/user_preview_views.xml',
        'views/user_preview_template_views.xml'
    ], 
    'demo': [], 
    'installable': True,
    'application': True,
    'auto_install': False,
} 