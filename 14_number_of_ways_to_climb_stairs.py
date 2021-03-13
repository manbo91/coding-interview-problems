"""
Hi, here's your problem today. This problem was recently asked by LinkedIn:

You are given a positive integer N which represents the number of steps in a
staircase. You can either climb 1 or 2 steps at a time. Write a function that
returns the number of unique ways to climb the stairs.
"""


def staircase(n):
    memo = {}

    def traverse(n, memo):
        if n < 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        if n in memo:
            return memo[n]

        memo[n] = traverse(n - 1, memo) + traverse(n - 2, memo)
        return memo[n]

    return traverse(n, memo)


print(staircase(4))
# 5
print(staircase(5))
# 8
print(staircase(10))
# 8

# Can you find a solution in O(n) time?
