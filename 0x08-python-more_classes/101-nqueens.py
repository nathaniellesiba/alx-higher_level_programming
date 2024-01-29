#!/usr/bin/python3

import sys

def is_safe(board, row, col, N):
    for i in range(row):
        if board[i] == col or \
            board[i] - i == col - row or \
            board[i] + i == col + row:
            return False
    return True

def solve_nqueens_util(board, row, N, solutions):
    if row == N:
        solutions.append(list(board))
    else:
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                solve_nqueens_util(board, row + 1, N, solutions)

def solve_nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)

    for solution in solutions:
        print(','.join(str(col) for col in solution))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    N = sys.argv[1]
    solve_nqueens(N)

