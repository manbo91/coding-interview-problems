"""
Hi, here's your problem today. This problem was recently asked by Twitter:

You are given the root of a binary tree. Find the level for the binary tree
with the minimum sum, and return that value.

For instance, in the example below, the sums of the trees are 10, 2 + 8 = 10,
and 4 + 1 + 2 = 7. So, the answer here should be 7.

class Node:
  def __init__(self, value, left=None, right=None):
    self.val = value
    self.left = left
    self.right = right

def minimum_level_sum(root):
  # Fill this in.

#     10
#    /  \
#   2    8
#  / \    \
# 4   1    2
node = Node(10)
node.left = Node(2)
node.right = Node(8)
node.left.left = Node(4)
node.left.right = Node(1)
node.right.right = Node(2)

print(minimum_level_sum(node))
# 7
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def minimum_level_sum(root):
    levels = {}
    traverse(root, 0, levels)
    minimum = float('inf')
    for _, value in levels.items():
        minimum = min(value, minimum)
    return minimum


def traverse(node, level, levels):
    if node is None:
        return

    levels[level] = levels.get(level, 0) + node.val
    traverse(node.left, level + 1, levels)
    traverse(node.right, level + 1, levels)


#     10
#    /  \
#   2    8
#  / \    \
# 4   1    2
node = Node(10)
node.left = Node(2)
node.right = Node(8)
node.left.left = Node(4)
node.left.right = Node(1)
node.right.right = Node(2)

print(minimum_level_sum(node))
# 7
