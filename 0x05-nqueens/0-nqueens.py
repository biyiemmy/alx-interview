#!/usr/bin/python3
""" N queens """
import sys


def solve_nqueens(n):
    """ soln """
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_safe(board, row, col):
        # Check if a queen can be placed at position
        # (row, col) without attacking any other queens
        for i in range(row):
            for i in range(row):
                if board[i] == col or \
                    board[i] - col == i - row or \
                        board[i] - col == row - i:
                    return False
        return True

    def place_queens(board, row):
        if row == n:
            print([[i, board[i]] for i in range(n)])
        else:
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    place_queens(board, row + 1)

    board = [-1] * n
    place_queens(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(n)
