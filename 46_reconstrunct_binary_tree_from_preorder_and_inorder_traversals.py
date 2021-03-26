"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

You are given the preorder and inorder traversals of a binary tree in the form
of arrays. Write a function that reconstructs the tree represented by these
traversals.

Example:
Preorder: [a, b, d, e, c, f, g]
Inorder: [d, b, e, a, f, c, g]

The tree that should be constructed from these traversals is:

    a
   / \
  b   c
 / \ / \
d  e f  g

Here's a start:

from collections import deque

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __str__(self):
    q = deque()
    q.append(self)
    result = ''
    while len(q):
      n = q.popleft()
      result += n.val
      if n.left:
        q.append(n.left)
      if n.right:
        q.append(n.right)

    return result


def reconstruct(preorder, inorder):
  # Fill this in.
"""
from collections import deque


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        q = deque()
        q.append(self)
        result = ''
        while len(q):
            n = q.popleft()
            result += n.val
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        return result


def reconstruct(preorder, inorder):
    """
    https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/
    """
    s = set()
    st = list()
    n = len(preorder)

    root = None

    pre = 0
    in_t = 0

    while pre < n:
        node = None

        while True:
            node = Node(preorder[pre])

            if root is None:
                root = node

            if len(st) > 0:
                if st[-1] in s:
                    s.discard(st[-1])
                    st[-1].right = node
                    st.pop()

                else:
                    st[-1].left = node

            st.append(node)

            if pre >= n or preorder[pre] == inorder[in_t]:
                pre += 1
                break
            pre += 1

        node = None

        while len(st) > 0 and in_t < n and st[-1].val == inorder[in_t]:
            node = st[-1]
            st.pop()
            in_t += 1

        if node is not None:
            s.add(node)
            st.append(node)

    return root


tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                   ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
print(tree)
# abcdefg
