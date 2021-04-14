"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given a list of integers, return the bounds of the minimum range that must be
sorted so that the whole list would be sorted.

Example:
Input: [1, 7, 9, 5, 7, 8, 10]
Output: (1, 5)
Explanation:
The numbers between index 1 and 5 are out of order and need to be sorted.

Here's your starting point:

def findRange(nums):
  # Fill this in.

print(findRange([1, 7, 9, 5, 7, 8, 10]))
# (1, 5)
"""


def findRange(nums):
    leftIdx = float('inf')
    rightIdx = float('-inf')

    i = 0
    while i < len(nums):
        if i > leftIdx and i < rightIdx:
            i = rightIdx + 1
            continue

        lIdx = i - 1
        while lIdx > 0 and nums[lIdx] > nums[i]:
            leftIdx = min(lIdx, leftIdx)
            lIdx -= 1

        rIdx = i + 1
        while rIdx < len(nums) and nums[rIdx] < nums[i]:
            rightIdx = max(rIdx, rightIdx)
            rIdx += 1

        i += 1

    return (leftIdx, rightIdx)


print(findRange([1, 7, 9, 5, 7, 8, 10]))
# (1, 5)
