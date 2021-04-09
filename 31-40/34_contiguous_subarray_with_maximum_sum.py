"""
Hi, here's your problem today. This problem was recently asked by Twitter:

You are given an array of integers. Find the maximum sum of all possible
contiguous subarrays of the array.

Example:

[34, -50, 42, 14, -5, 86]

Given this input array, the output should be 137. The contiguous subarray with
the largest sum is [42, 14, -5, 86].

Your solution should run in linear time.
"""

#def max_subarray_sum(arr):
#    pass


def max_subarray_sum(arr):
    max_sum = float('-inf')
    current_sum = max_sum

    for num in arr:
        if num > current_sum:
            current_sum = max(num, current_sum + num)
        else:
            current_sum += num
        max_sum = max(current_sum, max_sum)

    return max_sum


print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
# 137
print(max_subarray_sum([1, 1, 1, 2, 3]))
# 8
print(max_subarray_sum([-1, 1, -1, 2, -3]))
# 2
