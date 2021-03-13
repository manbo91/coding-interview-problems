"""
Hi, here's your problem today. This problem was recently asked by Amazon:

You are given a 2D array of integers. Print out the clockwise spiral traversal
of the matrix.

Example:

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

The clockwise spiral traversal of this array is:

1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12
"""


def matrix_spiral_print(M):
    traverse_spiral(M, 0, len(M[0]) - 1, 0, len(M) - 1)


def traverse_spiral(M, start_col, end_col, start_row, end_row):
    if start_col > end_col and start_row > end_row:
        return

    # left_top to right_top - 1
    for col in range(start_col, end_col):
        print(M[start_row][col])

    # right_top to bottom_right - 1
    for row in range(start_row, end_row):
        print(M[row][end_col])

    # bottom_right to bottom_left - 1
    for col in range(end_col, start_col, -1):
        print(M[end_row][col])

    # bottom_left to top_left - 1
    for row in range(end_row, start_row, -1):
        print(M[row][start_col])

    traverse_spiral(M, start_col + 1, end_col - 1, start_row + 1, end_row - 1)


grid = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
