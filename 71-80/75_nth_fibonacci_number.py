"""
Hi, here's your problem today. This problem was recently asked by Apple:

The Fibonacci sequence is the integer sequence defined by the recurrence
relation: F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1. In other words,
the nth Fibonacci number is the sum of the prior two Fibonacci numbers.
Below are the first few values of the sequence:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...

Given a number n, print the n-th Fibonacci Number.
Examples:
Input: n = 3
Output: 2

Input: n = 7
Output: 13
Here's a starting point:

class Solution():
  def fibonacci(self, n):
    # fill this in.

n = 9
print(Solution().fibonacci(n))
# 34
"""


class Solution():
    def fibonacci(self, n):
        memo = {0: 0, 1: 1}
        return self.fibonacciRecursive(n, memo)

    def fibonacciRecursive(self, n, memo):
        if n < 0:
            return 0
        if n in memo:
            return memo[n]
        memo[n] = self.fibonacciRecursive(
            n - 1, memo) + self.fibonacciRecursive(n - 2, memo)
        return memo[n]


n = 9
print(Solution().fibonacci(n))
# 34
