"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

You are given an lst of integers in an arbitrary order. Return whether or not
it is possible to make the lst non-decreasing by modifying at most 1 element
to any value.

We define an lst is non-decreasing if lst[i] <= lst[i + 1] holds for
every i (1 <= i < n).

Example:

[13, 4, 7] should return true, since we can modify 13 to any value 4 or less,
to make it non-decreasing.

[13, 4, 1] however, should return false, since there is no way to modify just
one element to make the lst non-decreasing.
"""


def check(lst):

    chance = True

    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            if chance:
                lst[i - 1] = lst[i]
                chance = False
            else:
                return False

    return True


print(check([13, 4, 7]))
# True
print(check([5, 1, 3, 2, 5]))
# False

# Can you find a solution in O(n) time?
