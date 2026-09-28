/** @odoo-module **/

import {Component, onWillStart, proxy} from "@odoo/owl";
import {registry} from "@web/core/registry";
import {rpc} from "@web/core/network/rpc";

export class SudokuApp extends Component {
    static template = "sudoku.AppTemplate";

    setup() {
        this.state = proxy({
            grid: Array(81).fill(0),
            initialGrid: Array(81).fill(0),
            solution: Array(81).fill(0),
            selectedCell: null,
            hintsRemaining: 3,
            difficulty: "easy",
            showSolveModal: false,
            isSolved: false,
            loading: true,
            statusMessage: "",
        });

        onWillStart(async () => {
            await this.startNewGame();
        });
    }

    async startNewGame() {
        this.state.loading = true;
        this.state.hintsRemaining = 3;
        this.state.selectedCell = null;
        this.state.isSolved = false;
        this.state.statusMessage = "";

        const data = await rpc("/sudoku/generate", {
            difficulty: this.state.difficulty,
        });

        this.state.grid = [...data.puzzle];
        this.state.initialGrid = [...data.puzzle];
        this.state.solution = [...data.solution];
        this.state.loading = false;
    }

    onDifficultyChange = (event) => {
        this.state.difficulty = event.target.value;
        this.startNewGame();
    };

    selectCell(index) {
        this.state.selectedCell = index;
    }

    handleInput(index, val) {
        if (this.state.initialGrid[index] !== 0 || this.state.isSolved) return;

        const num = parseInt(val, 10);
        if (isNaN(num) || num < 1 || num > 9) {
            this.state.grid[index] = 0;
        } else {
            this.state.grid[index] = num;
        }
        this.checkWinCondition();
    }

    checkWinCondition() {
        const isFull = !this.state.grid.includes(0);
        if (isFull) {
            const isCorrect = this.state.grid.every((val, idx) => val === this.state.solution[idx]);
            if (isCorrect) {
                this.state.isSolved = true;
                this.state.statusMessage = "Congratulations! Puzzle Solved!";
            } else {
                this.state.statusMessage = "Board full, but contains errors.";
            }
        }
    }

    useHint() {
        if (this.state.hintsRemaining <= 0 || this.state.isSolved) return;

        const emptyOrWrongIndices = [];
        for (let i = 0; i < 81; i++) {
            if (this.state.grid[i] !== this.state.solution[i]) {
                emptyOrWrongIndices.push(i);
            }
        }

        if (emptyOrWrongIndices.length > 0) {
            const randomIndex = emptyOrWrongIndices[Math.floor(Math.random() * emptyOrWrongIndices.length)];
            this.state.grid[randomIndex] = this.state.solution[randomIndex];
            this.state.hintsRemaining -= 1;
            this.checkWinCondition();
        }
    }

    confirmSolveBoard() {
        this.state.showSolveModal = true;
    }

    executeSolveBoard() {
        this.state.grid = [...this.state.solution];
        this.state.showSolveModal = false;
        this.state.isSolved = true;
        this.state.statusMessage = "Board solved automatically.";
    }

    closeModal() {
        this.state.showSolveModal = false;
    }

    skipBoard() {
        this.startNewGame();
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const root = document.getElementById("sudoku_app_root");
    if (root) {
        const env = registry.category("main_components").get("SudokuApp");
    }
});

registry.category("public_components").add("sudoku.App", SudokuApp);