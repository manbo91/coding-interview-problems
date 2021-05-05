"""
Hi, here's your problem today. This problem was recently asked by AirBNB:

Given a sorted list of positive numbers, find the smallest positive number
that cannot be a sum of any subset in the list.

Example:
Input: [1, 2, 3, 8, 9, 10]
Output: 7
Numbers 1 to 6 can all be summed by a subset of the list of numbers,
but 7 cannot.

def findSmallest(nums):
  # Fill this in.

print(findSmallest([1, 2, 3, 8, 9, 10]))
# 7
"""


def findSmallest(nums):
    res = 1
    for i in range(0, len(nums)):
        if nums[i] <= res:
            res = res + nums[i]
        else:
            break
    return res


print(findSmallest([1, 2, 3, 8, 9, 10]))
# 7

print(findSmallest([1, 3, 4, 5]))
# 2

print(findSmallest([1, 2, 6, 10, 11, 15]))
# 4
