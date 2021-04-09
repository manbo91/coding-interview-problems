"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given an array, nums, of n integers, find all unique triplets
(three numbers, a, b, & c) in nums such that a + b + c = 0.
Note that there may not be any triplets that sum to zero in nums,
and that the triplets must not be duplicates.

Example:
Input: nums = [0, -1, 2, -3, 1]
Output: [0, -1, 1], [2, -3, 1]
Here's a starting point:

class Solution(object):
  def threeSum(self, nums):
    # Fill this in.
"""

class Solution(object):
    def threeSum(self, nums):
        triplets = set()
        nums.sort()
        for i in range(len(nums) - 2):
            a = nums[i]
            if a > 0:
                break

            leftIdx = i + 1 
            rightIdx = len(nums) - 1
            while leftIdx < rightIdx:
                b = nums[leftIdx]
                c = nums[rightIdx]

                currentSum = a + b + c
                if currentSum == 0:
                    triplets.add((a, b, c))
                    leftIdx += 1
                    rightIdx -= 1
                elif currentSum < 0:
                    leftIdx += 1
                else:
                    rightIdx -= 1

        return [list(value) for value in triplets]
    
# Test Program
nums = [1, -2, 1, 0, 5]
print(Solution().threeSum(nums))
# [[-2, 1, 1]]
nums = [0, -1, 2, -3, 1]
print(Solution().threeSum(nums))
# [[0, -1, 1], [2, -3, 1]]
nums = [0, 0, 0]
print(Solution().threeSum(nums))
# [[0, 0, 0]]