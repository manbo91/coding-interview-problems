"""
Hi, here's your problem today. This problem was recently asked by Apple:

Implement a queue class using two stacks. A queue is a data structure that
supports the FIFO protocol (First in = first out). Your class should support
the enqueue and dequeue methods like a standard queue.
"""


class Queue:
    def __init__(self):
        self.stack = list()
        self.reversed_stack = list()

    def enqueue(self, val):
        self.stack.append(val)

    def dequeue(self):
        while len(self.stack) > 0:
            self.reversed_stack.append(self.stack.pop())
        return self.reversed_stack.pop()


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# 1 2 3
