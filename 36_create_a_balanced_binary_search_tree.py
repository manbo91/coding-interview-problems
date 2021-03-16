"""
Hi, here's your problem today. This problem was recently asked by LinkedIn:

Given a sorted list of numbers, change it into a balanced binary search tree.
You can assume there will be no duplicate numbers in the list.

Here's a starting point:

from collections import deque

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    # level-by-level pretty-printer
    nodes = deque([self])
    answer = ''
    while len(nodes):
      node = nodes.popleft()
      if not node:
        continue
      answer += str(node.value)
      nodes.append(node.left)
      nodes.append(node.right)
    return answer


def createBalancedBST(nums):
  # Fill this in.
"""

from collections import deque

RED = 'red'
BLACK = 'black'


class Node:
    def __init__(self, value, color):
        self.value = value
        self.left = None
        self.right = None
        self.color = color

    def __str__(self):
        # level-by-level pretty-printer
        nodes = deque([self])
        answer = ''
        while len(nodes):
            node = nodes.popleft()
            if not node:
                continue
            answer += str(node.value)
            nodes.append(node.left)
            nodes.append(node.right)
        return answer


class RedBlackTree:
    def __init__(self):
        self.root = None

    def put(self, value):
        self.root = self.putHelper(self.root, value)

    def isRed(self, node):
        if node is None:
            return False
        return node.color == RED

    def rotateLeft(self, node):
        temp = node.right
        node.right = temp.left
        temp.left = node
        temp.color = node.color
        node.color = RED
        return temp

    def rotateRight(self, node):
        temp = node.left
        node.left = temp.right
        temp.right = node
        temp.color = node.color
        node.color = RED
        return temp

    def flipColors(self, node):
        node.color = RED
        node.left.color = BLACK
        node.right.color = BLACK

    def putHelper(self, node, value):
        if node is None:
            return Node(value, RED)

        if value < node.value:
            node.left = self.putHelper(node.left, value)
        elif value > node.value:
            node.right = self.putHelper(node.right, value)

        _isRed = self.isRed
        if _isRed(node.right) and not _isRed(node.left):
            node = self.rotateLeft(node)
        if _isRed(node.left) and _isRed(node.left.left):
            node = self.rotateRight(node)
        if _isRed(node.left) and _isRed(node.right):
            self.flipColors(node)

        return node


def createBalancedBST(nums):
    RBT = RedBlackTree()
    for num in nums:
        RBT.put(num)
    return RBT.root


print(createBalancedBST([1, 2, 3, 4, 5, 6, 7]))
# 4261357
#   4
#  / \
# 2   6
#/ \ / \
#1 3 5 7
