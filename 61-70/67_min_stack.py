"""
Hi, here's your problem today. This problem was recently asked by Uber:

Design a simple stack that supports push, pop, top, and retrieving the minimum
element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Note: be sure that pop() and top() handle being called on an empty stack.

class minStack(object):
  def __init__(self):
    # Fill this in.

  def push(self, x):
    # Fill this in.

  def pop(self):
    # Fill this in.

  def top(self):
    # Fill this in.

  def getMin(self):
    # Fill this in.

x = minStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.getMin())
# -3
x.pop()
print(x.top())
# 0
print(x.getMin())
"""


class minStack(object):
    def __init__(self):
        self.stack = []
        self.min = []
        self.size = 0

    def push(self, x):
        if self.size == 0:
            self.min.append(x)
        else:
            if x <= self.min[-1]:
                self.min.append(x)
        self.stack.append(x)
        self.size += 1

    def pop(self):
        item = self.stack.pop()
        self.size -= 1
        if item == self.min[-1]:
            self.min.pop()

    def top(self):
        if self.size == 0:
            return None
        return self.stack[-1]

    def getMin(self):
        return self.min[-1]


x = minStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.getMin())
# -3
x.pop()
print(x.top())
# 0
print(x.getMin())
# -2
