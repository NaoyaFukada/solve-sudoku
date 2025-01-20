# Solve Sudoku 🔢

This Python application solves a Sudoku puzzle provided by the user. Simply enter the initial puzzle grid row by row, using 0 for empty cells, and the program will attempt to solve it.

## Features ✨

- **User-friendly input**: Prompts you to enter each row of your Sudoku puzzle.
- **Backtracking algorithm**: Uses a depth-first search approach to systematically fill in the valid numbers.
- **Single-solution solver**: Finds a solution if one exists and warns you if the puzzle is invalid or unsolvable.
- **Formatted output**: Displays the solved puzzle in a neat grid with borders.

## How to Run the Application 🏃‍♂️

1. Clone this repository:

   ```bash
   git clone https://github.com/NaoyaFukada/solve-sudoku.git
   cd solve-sudoku

   ```

2. Run the application:

   ```bash
   python3 index.py
   ```

3. Enter each row

   ```bash
   Enter numbers for each row, separated by commas (use 0 for empty cells):
   Row 1:
   ...
   ```

4. View the created sudoku:

   ```bash
   +-------+-------+-------+
   | 9 1 5 | 7 6 4 | 2 8 3 |
   | 3 4 8 | 5 9 2 | 7 1 6 |
   | 7 2 6 | 8 1 3 | 5 4 9 |
   +-------+-------+-------+
   | 2 7 1 | 4 3 9 | 8 6 5 |
   | 6 9 3 | 1 8 5 | 4 2 7 |
   | 8 5 4 | 6 2 7 | 9 3 1 |
   +-------+-------+-------+
   | 5 8 9 | 3 4 6 | 1 7 2 |
   | 4 6 7 | 2 5 1 | 3 9 8 |
   | 1 3 2 | 9 7 8 | 6 5 4 |
   +-------+-------+-------+
   ```
