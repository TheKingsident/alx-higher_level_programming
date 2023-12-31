#!/usr/bin/python3

"""
This module is a program that solves the N queens problem.
"""
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """
    Solve the N-Queens problem using backtracking.
    """
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def backtrack(col):
        if col >= n:
            solutions.append([(i, row.index(1))
                              for i, row in enumerate(board)][::-1])
            return

        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                backtrack(col + 1)
                board[i][col] = 0

    backtrack(0)

    return solutions


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(n)

    for solution in solutions:
        print([list(row) for row in solution])


if __name__ == "__main__":
    main()
