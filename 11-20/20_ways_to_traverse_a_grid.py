"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

You 2 integers n and m representing an n by m grid, determine the number of
ways you can get from the top-left to the bottom-right of the matrix y going
only right or down.

Example:
n = 2, m = 2

This should return 2, since the only possible routes are:
Right, down
Down, right.
"""


def num_ways(n, m):
    matrix = [[0] * n for _ in range(m)]

    def traverse(row, col):
        matrix[row][col] += 1
        if row == m and col == n:
            return
        if row < m - 1:
            traverse(row + 1, col)
        if col < n - 1:
            traverse(row, col + 1)

    traverse(0, 0)
    return matrix[-1][-1]


print(num_ways(2, 2))
# 2
print(num_ways(4, 4))
# 20
