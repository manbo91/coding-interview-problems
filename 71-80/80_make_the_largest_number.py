"""
Hi, here's your problem today. This problem was recently asked by Uber:

Given a number of integers, combine them so it would create the largest number.

Example:
Input:  [17, 7, 2, 45, 72]
Output:  77245217
def largestNum(nums):
  # Fill this in.

print(largestNum([17, 7, 2, 45, 72]))
# 77245217
"""


class largestNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


def largestNum(nums):
    largest_num = "".join(sorted(map(str, nums), key=largestNumKey))
    return '0' if largest_num[0] == '0' else largest_num


print(largestNum([17, 7, 2, 45, 72]))
# 77245217
