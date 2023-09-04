#!/usr/bin/python3

import sys

def is_safe(cbord, row, col):
    """
    Check if it's safe to place a queen at cbord[row][col].
    """
    # Check the left side of the current row
    for i in range(col):
        if cbord[row][i] == 1:
            return False
    
    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if cbord[i][j] == 1:
            return False
    
    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(cbord), 1), range(col, -1, -1)):
        if cbord[i][j] == 1:
            return False
    
    return True

def solve_nqueens(n):
    """
    Solve the N-Queens problem using backtracking.
    """
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    cbord = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def backtrack(col):
        if col >= n:
            # All queens are placed successfully, add this solution to the list
            solutions.append(["".join(["Q" if cell == 1 else "." for cell in row]) for row in cbord])
            return

        for i in range(n):
            if is_safe(cbord, i, col):
                cbord[i][col] = 1
                backtrack(col + 1)
                cbord[i][col] = 0

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
        for row in solution:
            print(row)
        print()

if __name__ == "__main__":
    main()
