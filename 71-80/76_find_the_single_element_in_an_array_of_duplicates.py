"""
Hi, here's your problem today. This problem was recently asked by Apple:

Given an array of integers, arr, where all numbers occur twice except one
number which occurs once, find the number.

Your solution should ideally be O(n) time and use constant extra space.

Example:
Input: arr = [7, 3, 5, 5, 4, 3, 4, 8, 8]
Output: 7

class Solution(object):
  def findSingle(self, nums):
    # Fill this in.

nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
print(Solution().findSingle(nums))
# 3
"""


class Solution(object):
    def findSingle(self, nums):
        num_dict = {}
        for num in nums:
            if num in num_dict:
                del num_dict[num]
            else:
                num_dict[num] = num

        for num in num_dict:
            return num


nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
print(Solution().findSingle(nums))
# 3
