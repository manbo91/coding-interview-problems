"""
Hi, here's your problem today. This problem was recently asked by Apple:

You are given the root of a binary tree. You need to implement 2 functions:

1. serialize(root) which serializes the tree into a string representation
2. deserialize(s) which deserializes the string back to the original tree
that it represents

For this problem, often you will be asked to design your own serialization
format. However, for simplicity, let's use the pre-order traversal of the
tree. Here's your starting point:

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def __str__(self):
    # pre-order printing of the tree.
    result = ''
    result += str(self.val)
    if self.left:
      result += str(self.left)
    if self.right:
      result += str(self.right)
    return result

def serialize(root):
  # Fill this in.

def deserialize(data):
  # Fill this in.

#     1
#    / \
#   3   4
#  / \   \
# 2   5   7
tree = Node(1)
tree.left = Node(3)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.right = Node(4)
tree.right.right = Node(7)
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        # pre-order printing of the tree.
        result = ''
        result += str(self.val)
        if self.left:
            result += str(self.left)
        if self.right:
            result += str(self.right)
        return result


def serialize(root):
    order = []
    stack = [root]
    traverse(stack, order)
    return "".join([str(x) + ' ' for x in order]).rstrip()


def traverse(stack, order):
    if len(stack) == 0:
        return

    node = stack.pop()
    if node is None:
        order.append('#')
    else:
        order.append(node.val)

        stack.append(node.left)
        traverse(stack, order)
        stack.append(node.right)
        traverse(stack, order)


def deserialize(data):
    order = [x for x in data.split() if x != '#']
    return "".join(order)


#     1
#    / \
#   3   4
#  / \   \
# 2   5   7
tree = Node(1)
tree.left = Node(3)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.right = Node(4)
tree.right.right = Node(7)

print(serialize(tree))
# 1 3 2 # # 5 # # 4 # 7 # #
print(deserialize('1 3 2 # # 5 # # 4 # 7 # #'))
# 132547
