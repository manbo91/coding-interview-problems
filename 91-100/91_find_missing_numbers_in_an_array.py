"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given an array of integers of size n, where all elements are between 1 and n inclusive,
find all of the elements of [1, n] that do not appear in the array.
Some numbers may appear more than once.

Example:
Input: [4,5,2,6,8,2,1,5]
Output: [3,7]
class Solution(object):
  def findDisappearedNumbers(self, nums):
    # Fill this in.

nums = [4, 6, 2, 6, 7, 2, 1]
print(Solution().findDisappearedNumbers(nums))
# [3, 5]
"""
class Solution(object):
  def findDisappearedNumbers(self, nums):
    nums_dict = {val:True for val in range(1,len(nums)+1)}
    for num in nums:
      if num in nums_dict:
        del nums_dict[num]
    return sorted([key for key in nums_dict])

nums = [4, 6, 2, 6, 7, 2, 1]
print(Solution().findDisappearedNumbers(nums))
# [3, 5]
