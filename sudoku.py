# 0 represents an empty cell

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


# Find empty cell
def find_empty():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


# Check whether number is valid
def valid(num, row, col):

    # Check row
    for j in range(9):
        if board[row][j] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


# Backtracking with constraint checking
def solve():

    empty = find_empty()

    if empty is None:
        return True

    row, col = empty

    for num in range(1, 10):

        if valid(num, row, col):

            board[row][col] = num

            if solve():
                return True

            # Backtracking
            board[row][col] = 0

    return False


# Main program
if solve():
    print("Sudoku Solution:")

    for row in board:
        print(row)
else:
    print("No solution exists!")