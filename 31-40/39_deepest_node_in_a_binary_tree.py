"""
Hi, here's your problem today. This problem was recently asked by Google:

You are given the root of a binary tree. Return the deepest node
(the furthest node from the root).

Example:

    a
   / \
  b   c
 /
d

The deepest node in this tree is d at depth 3.

Here's a starting point:

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        # string representation
        return self.val


def deepest(node):
    # Fill this in.
"""

from collections import deque


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        # string representation
        return self.val


def deepest(root):
    def traverse(queue, depth, deepest_node):
        if len(queue) == 0:
            return

        node = queue.pop()
        deepest_node[0] = node
        deepest_node[1] = depth

        if node.left is not None:
            queue.appendleft(node.left)
        if node.right is not None:
            queue.appendleft(node.right)

        traverse(queue, depth + 1, deepest_node)

    ans = [None, 0]
    queue = deque()
    queue.append(root)
    traverse(queue, 0, ans)
    [node, depth] = ans
    return node.val, depth


root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print(deepest(root))
# (d, 3)
