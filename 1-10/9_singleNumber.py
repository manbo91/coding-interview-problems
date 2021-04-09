"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Given a list of numbers, where every number shows up twice except for one number, find that one number.

Example:
Input: [4, 3, 2, 4, 1, 3, 2]
Output: 1

"""


def singleNumber(nums):
    nums_set = set()

    for num in nums:
        if num in nums_set:
            nums_set.remove(num)
        else:
            nums_set.add(num)

    for num in nums_set:
        return num


# average O(n) time | O(1) space
def singleNumber_upgrade(nums):
    left = 0
    right = len(nums) - 1

    while left <= right:

        target = nums[left]

        i = right
        while i > left and target != nums[i]:
            i -= 1

        if i == left:
            return nums[left]

        nums[i], nums[right] = nums[right], nums[i]

        left += 1
        right -= 1

    return None


print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
print(singleNumber_upgrade([4, 3, 2, 4, 1, 3, 2]))

# Challenge: Find a way to do this using O(1) memory.
