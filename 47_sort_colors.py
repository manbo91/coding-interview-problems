"""
Hi, here's your problem today. This problem was recently asked by Apple:

Given an array with n objects colored red, white or blue, sort them in-place
so that objects of the same color are adjacent, with the colors in the order red,
white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white,
and blue respectively.

Note: You are not suppose to use the library’s sort function for this problem.

Can you do this in a single pass?

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Here's a starting point:

class Solution:
  def sortColors(self, nums):
    # Fill this in.
"""


class Solution:
    def sortColors(self, nums):
        next_pos_0 = 0
        next_pos_2 = len(nums) - 1

        front_index = 0
        while front_index <= next_pos_2:
            if nums[front_index] == 0:
                self.swap(nums, front_index, next_pos_0)
                next_pos_0 += 1
                front_index += 1
            elif nums[front_index] == 2:
                self.swap(nums, front_index, next_pos_2)
                next_pos_2 -= 1
            else:
                front_index += 1

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]


nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

Solution().sortColors(nums)
print("After Sort: ")
print(nums)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
