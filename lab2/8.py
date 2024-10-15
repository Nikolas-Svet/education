def solve_sudoku(matrix):
    empty = find_empty(matrix)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 5):
        if is_valid(matrix, num, row, col):
            matrix[row][col] = num
            if solve_sudoku(matrix):
                return True
            matrix[row][col] = 0
    return False

def find_empty(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                return (i, j)
    return None

def is_valid(matrix, num, row, col):
    if num in matrix[row]:
        return False
    for i in range(4):
        if matrix[i][col] == num:
            return False
    start_row = (row // 2) * 2
    start_col = (col // 2) * 2
    for i in range(2):
        for j in range(2):
            if matrix[start_row + i][start_col + j] == num:
                return False
    return True

def print_matrix(matrix):
    for row in matrix:
        print(''.join(str(num) for num in row))

sudoku = [
    [0, 0, 0, 0],
    [0, 0, 2, 0],
    [0, 1, 0, 0],
    [3, 0, 0, 4]
]

if solve_sudoku(sudoku):
    print("Решенное судоку:")
    print_matrix(sudoku)
else:
    print("Нет решения")
