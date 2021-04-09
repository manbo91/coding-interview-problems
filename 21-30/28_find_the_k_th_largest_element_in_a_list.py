"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Given a list, find the k-th largest element in the list.
Input: list = [3, 5, 2, 4, 6, 8], k = 3
Output: 5
"""


def findKthLargest(nums, k):
    largest_array = [float('-inf') for _ in range(k)]

    for num in nums:
        if num > largest_array[0]:
            largest_array[0] = num
            largest_array.sort()

    return largest_array[0]


print(findKthLargest([3, 5, 2, 4, 6, 8], 3))
# 5
