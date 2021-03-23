"""
Hi, here's your problem today. This problem was recently asked by Amazon:

Given a binary tree, return all values given a certain height h.

Here's a starting point:

class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def valuesAtHeight(root, height):
  # Fill this in.

#     1
#    / \
#   2   3
#  / \   \
# 4   5   7
"""

from collections import deque


class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def valuesAtHeight(root, height):
    values = list()
    queue = deque()
    queue.appendleft((root, 1))
    traverse(queue, height, values)
    return values


def traverse(queue, height, values):
    if len(queue) == 0:
        return

    node, h = queue.pop()
    if h > height:
        return
    if h == height:
        values.append(node.value)

    if node.left:
        queue.appendleft((node.left, h + 1))
    if node.right:
        queue.appendleft((node.right, h + 1))
    traverse(queue, height, values)


a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print(valuesAtHeight(a, 3))
# [4, 5, 7]
