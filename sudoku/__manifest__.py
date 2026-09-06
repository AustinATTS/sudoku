# -*- coding: utf-8 -*-
# Part of Baker's Sudoku. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sudoku',
    'version': '0.2.2',
    'category': 'Website',
    'website': 'https://www.toastysoftware.co.uk/journal/sudoku-8',
    'summary': 'Interactive Sudoku game powered by OWL and Python algorithms',
    'depends': ['web', 'website'],
    'description': """
Sudoku for Odoo 19
==================

Enjoy a fresh batch of daily Sudoku puzzles right inside your Odoo Website! 
Featuring a warm bakery theme, intelligent board generation, multiple difficulty 
levels, and interactive helper tools.

Key Features:
-------------
* **Custom Sudoku Generator:** Endless uniquely solvable puzzles generated in Python.
* **4 Difficulty Tiers:** Easy, Medium, Hard, and Extremely Difficult.
* **Smart Hints:** Get up to 3 automated hints per board.
* **Interactive OWL 3 UI:** Built using Odoo's modern Web Library for instant response times.
* **Auto-Solve Confirmation:** Safely reveal the full solution without accidental clicks.
    """,
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
