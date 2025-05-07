def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def bound(board, row, n):
    # No need to go beyond the row limit
    return row < n

def solve_nqueens_branch_bound(board, row, n):
    if row == n:
        # Found a solution
        for i in range(n):
            print("." * board[i] + "Q" + "." * (n - board[i] - 1))
        print()
        return True

    res = False
    for col in range(n):
        if is_safe(board, row, col) and bound(board, row, n):
            board[row] = col
            res = solve_nqueens_branch_bound(board, row + 1, n) or res

    return res

def n_queens_branch_bound(n):
    board = [-1] * n
    solve_nqueens_branch_bound(board, 0, n)

# Test Branch and Bound Solution for n=4
print("Branch and Bound Solution for N=4:")
n_queens_branch_bound(4)
