"""
Hi, here's your problem today. This problem was recently asked by Facebook:

You are given the root of a binary search tree. Return true if it is a valid
binary search tree, and false otherwise. Recall that a binary search tree has
the property that all keys in the left subtree are less than or equal to the
root, and all keys in the right subtree are greater than or equal to the root.

Here's a starting point:

class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

def is_bst(root):
  # Fill this in.
"""


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


def is_bst(root):
    if root is None:
        return True

    if root.left is not None and root.left.key > root.key:
        return False
    if root.right is not None and root.right.key <= root.key:
        return False

    is_valid_left = is_bst(root.left)
    if is_valid_left is False:
        return False
    is_valid_right = is_bst(root.right)
    if is_valid_right is False:
        return False

    return True


a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)
print(is_bst(a))
# True
