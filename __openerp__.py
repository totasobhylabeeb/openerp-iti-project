{
    'name': 'project',
    'version': '1.0',
    'summary': 'iti openerp project first version',
    'website': 'http://wwww.iti.gov.eg',
    'description': 'Basic example of  iti module',
    'auther': 'niven-ahmed-aya-tahany-fatma',
    'depends': ['base', 'hr', 'warehouse'],
    'data': [
        'project_view.xml',
        'security/iti_security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
}
