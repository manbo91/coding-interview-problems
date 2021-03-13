"""
Hi, here's your problem today. This problem was recently asked by Uber:

Given a list of numbers, find if there exists a pythagorean triplet in that list.
A pythagorean triplet is 3 variables a, b, c where a2 + b2 = c2

Example:
Input: [3, 5, 12, 5, 13]
Output: True
Here, 5^2 + 12^2 = 13^2.
"""


def findPythagoreanTriplets(nums):

    # -> You always have to find exactly position in the range.
    for i in range(1, len(nums) - 1):

        front = nums[i - 1]
        back = nums[i]

        front_pow = pow(front, 2)
        back_pow = pow(back, 2)

        result_index = i + 1

        while result_index < len(nums):
            result = nums[result_index]

            if pow(result, 2) == (front_pow + back_pow):
                return True

            result_index += 1

    return False


print(findPythagoreanTriplets([3, 12, 5, 13]))
print(findPythagoreanTriplets([3, 5, 6, 11, 12, 5, 13]))
