"""
Hi, here's your problem today. This problem was recently asked by Twitter:

You are given the root of a binary tree. Find and return the largest subtree
of that tree, which is a valid binary search tree.

Here's a starting point:

class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

  def __str__(self):
    # preorder traversal
    answer = str(self.key)
    if self.left:
      answer += str(self.left)
    if self.right:
      answer += str(self.right)
    return answer

def largest_bst_subtree(root):
  # Fill this in.
"""


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def __str__(self):
        # preorder traversal
        answer = str(self.key)
        if self.left:
            answer += str(self.left)
        if self.right:
            answer += str(self.right)
        return answer


def largest_bst_subtree(root):
    largest_bst = [None, 0]
    largest_bst_subtree_recursive(node.left, largest_bst)
    largest_bst_subtree_recursive(node.right, largest_bst)
    return largest_bst[0]


def largest_bst_subtree_recursive(node, largest_bst):
    if node is None:
        return 0
    count = 1
    count += largest_bst_subtree_recursive(node.left, largest_bst)
    count += largest_bst_subtree_recursive(node.right, largest_bst)
    if count > largest_bst[1]:
        largest_bst[1] = count
        largest_bst[0] = node
    return count


#     5
#    / \
#   6   7
#  /   / \
# 2   4   9
node = TreeNode(5)
node.left = TreeNode(6)
node.right = TreeNode(7)
node.left.left = TreeNode(2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(9)
print(largest_bst_subtree(node))
#749
