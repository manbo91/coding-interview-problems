"""
Hi, here's your problem today. This problem was recently asked by LinkedIn:

Write a function that reverses the digits a 32-bit signed integer, x. Assume
that the environment can only store integers within the 32-bit signed integer
range, [-2^31, 2^31 - 1]. The function returns 0 when the reversed integer
overflows.

Example:
Input: 123
Output: 321

class Solution:
  def reverse(self, x):
    # Fill this in.

print(Solution().reverse(123))
# 321
print(Solution().reverse(2**31))
# 0
"""


class Solution:
    def reverse(self, x):
        isNegative = True if x < 0 else False
        if (isNegative): x *= -1

        length = 0
        temp = x
        while temp > 10:
            temp = temp // 10
            length += 1

        reversedDigit = 0
        while x > 10:
            r = x % 10
            x = x // 10
            reversedDigit += r * (10**length)
            if (reversedDigit > 2**31):
                return 0
            length -= 1

        reversedDigit += x
        return reversedDigit if not isNegative else reversedDigit * -1


print(Solution().reverse(123))
# 321
print(Solution().reverse(2**31))
# 0
print(Solution().reverse(-54321))
# -12345
