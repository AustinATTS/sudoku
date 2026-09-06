# -*- coding: utf-8 -*-
# Part of Baker's Sudoku. See LICENSE file for full copyright and licensing details.

import random


def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def count_solutions(board, count=0):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        count = count_solutions(board, count)
                        board[row][col] = 0
                        if count >= 2:
                            return count
                return count
    return count + 1


def generate_full_board():
    board = [[0] * 9 for _ in range(9)]

    def fill_grid(b):
        for row in range(9):
            for col in range(9):
                if b[row][col] == 0:
                    nums = list(range(1, 10))
                    random.shuffle(nums)
                    for num in nums:
                        if is_valid(b, row, col, num):
                            b[row][col] = num
                            if fill_grid(b):
                                return True
                            b[row][col] = 0
                    return False
        return True

    fill_grid(board)
    return board


def generate_puzzle(difficulty="easy"):
    clue_targets = {
        'easy': 42,
        'medium': 34,
        'hard': 28,
        'extreme': 22
    }
    target_clues = clue_targets.get(difficulty, 36)

    solution = generate_full_board()
    puzzle = [row[:] for row in solution]

    cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(cells)

    current_clues = 81
    for r, c in cells:
        if current_clues <= target_clues:
            break

        temp = puzzle[r][c]
        puzzle[r][c] = 0

        board_copy = [row[:] for row in puzzle]
        if count_solutions(board_copy) != 1:
            puzzle[r][c] = temp
        else:
            current_clues -= 1

    flat_puzzle = [cell for row in puzzle for cell in row]
    flat_solution = [cell for row in solution for cell in row]

    return flat_puzzle, flat_solution
