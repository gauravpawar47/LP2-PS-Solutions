def is_safe(board, row, col, n):
    # Check column and diagonals for safety
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, n):
    if row == n:
        # A solution is found, print it
        for i in range(n):
            print("." * board[i] + "Q" + "." * (n - board[i] - 1))
        print()
        return True
    
    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            res = solve_nqueens(board, row + 1, n) or res
    
    return res

def n_queens_backtracking(n):
    board = [-1] * n
    solve_nqueens(board, 0, n)

# Test the Backtracking Solution for n=4
print("Backtracking Solution for N=4:")
n_queens_backtracking(4)
