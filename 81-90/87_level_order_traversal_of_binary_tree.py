"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

Given the root of a binary tree, print its level-order traversal. For example:

  1
 / \
2   3
   / \
  4   5

The following tree should output 1, 2, 3, 4, 5.

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def print_level_order(root):
  # Fill this in.

root = Node(1, Node(2), Node(3, Node(4), Node(5)))
print_level_order(root)
# 1 2 3 4 5
"""

from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_level_order(root):
    queue = deque([root])
    order = []
    while len(queue) > 0:
        node = queue.pop()
        order.append(node.val)
        if node.left:
            queue.appendleft(node.left)
        if node.right:
            queue.appendleft(node.right)

    print(" ".join([str(x) for x in order]))


root = Node(1, Node(2), Node(3, Node(4), Node(5)))
print_level_order(root)
# 1 2 3 4 5
