"""
Hi, here's your problem today. This problem was recently asked by LinkedIn:

Given a non-empty array where each element represents a digit of a non-negative integer,
add one to the integer. The most significant digit is at the front of the array and each
element in the array contains only one digit. Furthermore, the integer does not have
leading zeros, except in the case of the number '0'.

Example:
Input: [2,3,4]
Output: [2,3,5]
class Solution():
  def plusOne(self, digits):
    # Fill this in.

num = [2, 9, 9]
print(Solution().plusOne(num))
# [3, 0, 0]
"""


class Solution():
    def plusOne(self, digits):
        index = len(digits) - 1
        while index >= 0 and digits[index] + 1 == 10:
            digits[index] = 0
            index -= 1

        if index == -1:
            digits.insert(0, 1)
        else:
            digits[index] += 1
        
        return digits


num = [2, 9, 9]
print(Solution().plusOne(num))
# [3, 0, 0]

num = [2, 3, 4]
print(Solution().plusOne(num))
# [2, 3, 5]

num = [9, 9, 9]
print(Solution().plusOne(num))
# [1, 0, 0, 0]