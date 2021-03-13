"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

You are given an array of integers. Return the largest product that can be made
by multiplying any 3 integers in the array.

Example:

[-4, -4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128.
"""


def maximum_product_of_three(lst):
    if len(lst) == 3:
        return lst[0] * lst[1] * lst[2]

    lst.sort()
    negative = []
    negative_index = 0
    while lst[negative_index] < 0 and len(negative) < 2:
        negative.append(lst[negative_index])
        negative_index += 1

    positive = []
    positive_index = len(lst) - 1
    while lst[positive_index] > 0 and len(positive) < 3:
        positive.append(lst[positive_index])
        positive_index -= 1

    largest = float('-inf')
    negative_value = None

    if len(negative) == 2:
        negative_value = negative[0] * negative[1]
        for num in positive:
            largest = max(negative_value * num, largest)

    if negative_value is None:
        largest = positive[0] * positive[1] * positive[2]
    else:
        positive_value = positive[0] * positive[1]
        for num in positive:
            largest = max(positive_value * num, largest)

    return largest


print(maximum_product_of_three([-4, -4, 2, 8]))
# 128
print(maximum_product_of_three([-4, 2, 8]))
# -64
print(maximum_product_of_three([1, 2, 8]))
# 16
print(maximum_product_of_three([9, 10, 1, 2, 8]))
# 720
print(maximum_product_of_three([-10, -10, 4, 9, -2]))
# 900
