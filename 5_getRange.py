"""
Hi, here's your problem today. This problem was recently asked by AirBNB:

Given a sorted array, A, with possibly duplicated elements, find the indices
of the first and last occurrences of a target element, x. Return -1 if the target is not found.

Example:

Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150
Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9
Output: [-1, -1]
"""


def binary_search_range(arr, target, start_index, end_index):
    if start_index > end_index:
        return [-1, -1]

    mid_index = (start_index + end_index) // 2
    mid_element = arr[mid_index]

    if target == mid_element:
        left_index = mid_index - 1
        while left_index > 0 and arr[left_index] == target:
            left_index -= 1
        left_index += 1

        right_index = mid_index + 1
        while right_index < len(arr) and arr[right_index] == target:
            right_index += 1
        right_index -= 1

        return [left_index, right_index]

    elif target < mid_element:
        return binary_search_range(arr, target, start_index, mid_index - 1)
    else:
        return binary_search_range(arr, target, mid_index + 1, end_index)


class Solution:
    def getRange(self, arr, target):
        start_index = 0
        end_index = len(arr)
        return binary_search_range(arr, target, start_index, end_index)


# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(Solution().getRange(arr, x))
# [1, 4]

arr = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
x = 9
print(Solution().getRange(arr, x))
# [6,8]

arr = [100, 150, 150, 153]
x = 150
print(Solution().getRange(arr, x))
# [1, 2]

arr = [1, 2, 3, 4, 5, 6, 10]
x = 9
print(Solution().getRange(arr, x))
# [-1, -1]
