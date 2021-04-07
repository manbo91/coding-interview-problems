"""
Hi, here's your problem today. This problem was recently asked by Amazon:

You are given an array of integers. Return an array of the same size where
the element at each index is the product of all the elements in the original
array except for the element at that index.

For example, an input of [1, 2, 3, 4, 5] should return [120, 60, 40, 30, 24].

You cannot use division in this problem.

Here's a start:

def products(nums):
  # Fill this in.
"""


def products(nums):
    numsLeftToRight = [1 for _ in range(len(nums))]
    numsRightToLeft = [1 for _ in range(len(nums))]

    for i in range(1, len(nums)):
        numsLeftToRight[i] = numsLeftToRight[i - 1] * nums[i - 1]
    for i in range(len(nums) - 2, -1, -1):
        numsRightToLeft[i] = numsRightToLeft[i + 1] * nums[i + 1]

    return [numsLeftToRight[i] * numsRightToLeft[i] for i in range(len(nums))]


print(products([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]
