sudoku = []

def ask_for_sudoku():
    print("Enter numbers for each row, separated by commas (use 0 for empty cells):")
    for i in range(9):
        row = input(f"Row {i + 1}: ")
        sudoku.append(list(map(int, row.split(","))))

def find_possible_nums(sudoku, row, col):
    possible_nums = list(range(1, 10))

    for c in range(9):
        if sudoku[row][c] in possible_nums:
            possible_nums.remove(sudoku[row][c])

    for r in range(9):
        if sudoku[r][col] in possible_nums:
            possible_nums.remove(sudoku[r][col])
    
    for r in range((row // 3) * 3, (row // 3) * 3 + 3):
        for c in range((col // 3) * 3, (col // 3) * 3 + 3):
            if sudoku[r][c] in possible_nums:
                possible_nums.remove(sudoku[r][c])
    
    return possible_nums

def solve_sudoku(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                possible_nums = find_possible_nums(sudoku, row, col)
                for num in possible_nums:
                    sudoku[row][col] = num
                    if solve_sudoku(sudoku):
                        return True
                    sudoku[row][col] = 0
                return False
    return True

def print_sudoku_with_outer_grid(sudoku):
    print("+" + "-------+" * 3)  # Top border of the grid
    for row in range(9):
        for col in range(9):
            if col == 0:  # Left border
                print("|", end=" ")
            print(sudoku[row][col], end=" ")
            if (col + 1) % 3 == 0:  # Vertical inner grid line
                print("|", end=" ")
        print()  # Move to the next row
        if (row + 1) % 3 == 0:  # Horizontal inner grid line
            print("+" + "-------+" * 3)

ask_for_sudoku()
if solve_sudoku(sudoku):
    print_sudoku_with_outer_grid(sudoku)
else:
    print("This sudoku is not valid")