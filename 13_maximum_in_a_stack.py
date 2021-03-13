"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Implement a class for a stack that supports all the regular functions (push, pop)
and an additional function of max() which returns the maximum element in the
stack (return None if the stack is empty). Each method should run in constant time.
"""

import heapq


class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxHeap = []

    def push(self, val):
        self.stack.append(val)
        heapq.heappush(self.maxHeap, (val * -1))

    def pop(self):
        delete_val = self.stack.pop()
        self.maxHeap.remove(delete_val * -1)
        return delete_val

    def max(self):
        return self.maxHeap[0] * -1


s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
