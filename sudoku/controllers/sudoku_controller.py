from odoo import http
from odoo.http import request

from ..utils.sudoku_generator import generate_puzzle


class SudokuController(http.Controller):

    @http.route('/sudoku/game_page', type='http', auth='public', website=True)
    def game_page(self):
        return request.render(
            'sudoku.game_page',
            {
                'session_info': request.env['ir.http'].get_frontend_session_info(),
            }
        )

    @http.route('/sudoku/generate', type='json', auth='public', website=True)
    def generate_board(self, difficulty='easy'):
        puzzle, solution = generate_puzzle(difficulty)
        return {
            'puzzle': puzzle,
            'solution': solution,
        }
