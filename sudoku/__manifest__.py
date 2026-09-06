{
    'name': 'Sudoku',
    'version': '0.1.0',
    'category': 'Austin ATTS',
    'website': 'https://www.austinatts.co.uk',
    'summary': 'Interactive Sudoku game powered by OWL and Python algorithms',
    'depends': ['web', 'website'],
    'currency': 'EUR',
    'price': 0.00,
    'data': [
        'views/sudoku_game_page_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'sudoku/static/src/scss/sudoku.scss',
            'sudoku/static/src/js/sudoku_app.js',
            'sudoku/static/src/xml/app_template.xml',
        ],
    },
    'author': 'Austin Welsh-Graham',
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}