"""
Hi, here's your problem today. This problem was recently asked by Amazon:

Given an array of n positive integers and a positive integer s, find the minimal
length of a contiguous subarray of which the sum ≥ s.
If there isn't one, return 0 instead.

Example:
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
"""


class Solution:
    def minSubArrayLen(self, nums, s):
        minimal_length = float('inf')

        left = 0
        right = 0
        while left < len(nums) and right <= len(nums):

            current_sum = sum(nums[left:right + 1])
            if current_sum == s:
                minimal_length = min((right - left + 1), minimal_length)
                left = right
                right = left
            elif current_sum < s:
                right += 1
            else:
                left += 1

        return minimal_length if minimal_length != float('inf') else 0


print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
# 2
print(Solution().minSubArrayLen([0, 0, 0], 7))
# 0
print(Solution().minSubArrayLen([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7], 42))
# 11
