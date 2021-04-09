"""
Hi, here's your problem today. This problem was recently asked by Apple:

Given an integer k and a binary search tree, find the floor (less than or equal to) of k,
and the ceiling (larger than or equal to) of k. If either does not exist, then print them
as None.

Here is the definition of a node for the tree.
"""


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def findCeilingFloor(root_node, k, floor=None, ceil=None):
    if root_node == None:
        return (floor, ceil)

    node = root_node

    if floor is None and node.value <= k:
        floor = node.value
    if ceil is None and node.value >= k:
        ceil = node.value

    if floor is not None and floor < node.value <= k:
        floor = node.value
    elif floor is not None and node.value < floor:
        return (floor, ceil)
    if ceil is not None and ceil > node.value >= k:
        ceil = node.value
    elif ceil is not None and node.value > ceil:
        return (floor, ceil)

    left_floor, left_ceil = findCeilingFloor(node.left, k, floor, ceil)
    right_floor, right_ceil = findCeilingFloor(node.right, k, floor, ceil)

    if left_floor is not None and right_floor is not None:
        floor = left_floor if k-left_floor < k-right_floor else right_floor
    elif left_floor is not None:
        floor = left_floor
    elif right_floor is not None:
        floor = right_floor

    if left_ceil is not None and right_ceil is not None:
        ceil = left_ceil if left_ceil-k < right_ceil-k else right_ceil
    elif left_ceil is not None:
        ceil = left_ceil
    elif right_ceil is not None:
        ceil = right_ceil

    return (floor, ceil)


root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

print(findCeilingFloor(root, 5))
# (4, 6)

root = Node(1)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

print(findCeilingFloor(root, 13))
# (12, 14)
