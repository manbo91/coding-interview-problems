"""
Hi, here's your problem today. This problem was recently asked by Google:

Given a list of numbers with only 3 unique numbers (1,2,3), sort the list O(n) time.

Example 1:
Input: [3, 3, 2, 1, 3, 2, 1]
Output: [1, 1, 2, 2, 3, 3, 3]
"""


def sortNums(nums):
    next_pos_1 = 0
    next_pos_3 = len(nums) - 1

    for i in range(len(nums)):
        if nums[i] == 3:
            if i > next_pos_3:
                break

            nums[i] = nums[next_pos_3]
            nums[next_pos_3] = 3
            next_pos_3 -= 1

        if nums[i] == 1:
            nums[i] = nums[next_pos_1]
            nums[next_pos_1] = 1
            next_pos_1 += 1

    return nums


print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]
print(sortNums([1, 1, 2, 2, 3, 3, 3, 3, 2, 2, 1, 1, 2, 2]))
# [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3]
