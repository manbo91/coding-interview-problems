"""
Hi, here's your problem today. This problem was recently asked by Amazon:

You are given a 2D array of characters, and a target string. Return whether
or not the word target word exists in the matrix. Unlike a standard word search,
the word must be either going left-to-right, or top-to-bottom in the matrix.

Example:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

Given this matrix, and the target word FOAM, you should return true, as it can
be found going up-to-down in the first column.
"""


def word_search(matrix, word):
    row, col = find_first_match(matrix, word[0])

    left_to_right = True
    top_to_bottom = True

    for i, char in enumerate(word):
        if row == 0:
            if matrix[i][col] != char:
                top_to_bottom = False
        if col == 0:
            if matrix[row][i] != char:
                left_to_right = False

    return left_to_right or top_to_bottom


def find_first_match(matrix, character):
    max_row = len(matrix)
    max_col = len(matrix[0])

    for row in range(max_row):
        if matrix[row][0] == character:
            return row, 0

    for col in range(max_col):
        if matrix[0][col] == character:
            return 0, col


matrix = [['F', 'A', 'C', 'I'], ['O', 'B', 'Q', 'P'], ['A', 'N', 'O', 'B'],
          ['M', 'A', 'S', 'S']]

print(word_search(matrix, "FOAM"))
# True
print(word_search(matrix, "ABNA"))
# True
print(word_search(matrix, "FAIC"))
# True
