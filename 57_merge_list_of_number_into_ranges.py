"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Given a sorted list of numbers, return a list of strings that represent all
of the consecutive numbers.

Example:
Input: [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
Output: ['0->2', '5->5', '7->11', '15->15']
Assume that all numbers will be greater than or equal to 0, and each element
can repeat.

Here is a starting point:

def findRanges(nums):
  # Fill this in.
"""


def findRanges(nums):
    ranges = list()
    start = nums[0]
    for i in range(len(nums) - 1):
        num1 = nums[i]
        num2 = nums[i + 1]
        if num2 - num1 <= 1:
            continue
        else:
            ranges.append([f"{start}->{num1}"])
            start = num2

    ranges.append([f"{start}->{nums[-1]}"])
    return ranges


print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0->2', '5->5', '7->11', '15->15']
print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11]))
# ['0->2', '5->5', '7->11']
print(findRanges([0]))
# ['0->0']
