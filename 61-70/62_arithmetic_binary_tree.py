"""
Hi, here's your problem today. This problem was recently asked by Apple:

You are given a binary tree representation of an arithmetic expression.
In this tree, each leaf is an integer value,, and a non-leaf node is one of
the four operations: '+', '-', '*', or '/'.

Write a function that takes this tree and evaluates the expression.

Example:

    *
   / \
  +    +
 / \  / \
3  2  4  5

This is a representation of the expression (3 + 2) * (4 + 5), and should
return 45.

Here's a starting point:

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def evaluate(root):
  # Fill this in.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"


def evaluate(root):
    result = 0
    if root.val == PLUS:
        result = evaluate(root.left) + evaluate(root.right)
    elif root.val == MINUS:
        result = evaluate(root.left) - evaluate(root.right)
    elif root.val == TIMES:
        result = evaluate(root.left) * evaluate(root.right)
    elif root.val == DIVIDE:
        result = evaluate(root.left) / evaluate(root.right)
    else:
        return root.val
    return result


tree = Node(TIMES)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node(PLUS)
tree.right.left = Node(4)
tree.right.right = Node(5)
print(evaluate(tree))
# 45
