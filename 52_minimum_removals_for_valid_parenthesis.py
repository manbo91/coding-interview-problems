"""
Hi, here's your problem today. This problem was recently asked by Uber:

You are given a string of parenthesis. Return the minimum number of parenthesis
that would need to be removed in order to make the string valid. "Valid" means
that each open parenthesis has a matching closed parenthesis.

Example:

"()())()"

The following input should return 1.

")("

Here's a start:

def count_invalid_parenthesis(string):
  # Fill this in.
"""


def count_invalid_parenthesis(string):
    count = 0
    stack = list()
    for token in string:
        if token == "(":
            stack.append(token)
        elif token == ")":
            if len(stack) == 0:
                count += 1
            else:
                stack.pop()
    return count + len(stack)


print(count_invalid_parenthesis("()())()"))
# 1
print(count_invalid_parenthesis("(((())))"))
# 0
print(count_invalid_parenthesis("((()())))))))))))))))()"))
# 13
