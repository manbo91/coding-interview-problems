"""
Hi, here's your problem today. This problem was recently asked by LinkedIn:

Given a 2-dimensional grid consisting of 1's (land blocks) and 0's (water blocks),
count the number of islands present in the grid. The definition of an island is as follows:
1.) Must be surrounded by water blocks.
2.) Consists of land blocks (1's) connected to adjacent land blocks
(either vertically or horizontally).
Assume all edges outside of the grid are water.

Example:
Input:
10001
11000
10110
00000

Output: 3
Here's your starting point:

class Solution(object):
  def inRange(self, grid, r, c):
    numRow, numCol = len(grid), len(grid[0])
    if r < 0 or c < 0 or r >= numRow or c >= numCol:
      return False
    return True

  def numIslands(self, grid):
    # Fill this in.
"""


class Solution(object):
    def inRange(self, grid, r, c):
        numRow, numCol = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= numRow or c >= numCol:
            return False
        return True

    def numIslands(self, grid):
        w = len(grid[0])
        h = len(grid)
        matrix = [[None for _ in range(w)] for _ in range(h)]
        count = 0
        for row in range(h):
            for col in range(w):
                if matrix[row][col] is None:
                    if grid[row][col] == 1:
                        self.traverseIslands(grid, row, col, row * w + col,
                                             matrix)
                        count += 1
                    else:
                        matrix[row][col] = False
        return count

    def traverseIslands(self, grid, row, col, index, matrix):
        if self.inRange(grid, row, col):
            if matrix[row][col] is not None:
                return

            if grid[row][col] == 1:
                matrix[row][col] = index
                self.traverseIslands(grid, row + 1, col, index, matrix)
                self.traverseIslands(grid, row, col + 1, index, matrix)
                self.traverseIslands(grid, row - 1, col, index, matrix)
                self.traverseIslands(grid, row, col - 1, index, matrix)


grid = [[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [1, 0, 0, 1, 1], [0, 0, 0, 0, 0]]
print(Solution().numIslands(grid))
# 3
