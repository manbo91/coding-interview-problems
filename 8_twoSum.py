"""
Hi, here's your problem today. This problem was recently asked by Facebook:

You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.

Example:
Given [4, 7, 1 , -3, 2] and k = 5,
return true since 4 + 1 = 5.
"""


def two_sum(list, k):
    list.sort()

    front = 0
    back = len(list) - 1
    while front < back:
        current_sum = list[front] + list[back]

        if current_sum == k:
            return [list[front], list[back]]
        elif current_sum < k:
            front += 1
        else:
            back -= 1

    return [-1, -1]


print(two_sum([4, 7, 1, -3, 2], 5))
