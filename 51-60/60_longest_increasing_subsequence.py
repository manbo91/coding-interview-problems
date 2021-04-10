"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

You are given an array of integers. Return the length of the longest increasing
subsequence (not necessarily contiguous) in the array.

Example:
[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

The following input should return 6 since
the longest increasing subsequence is 0, 2, 6, 9, 11, 15.
"""


def solution(items):
    lookup_table = [items[0]]
    for i in range(1, len(items)):
        item = items[i]
        if item > lookup_table[-1]:
            lookup_table.append(item)
            continue

        index = binary_search(lookup_table, 0, len(lookup_table), item)
        if item < lookup_table[index]:
            lookup_table[index] = item

    return len(lookup_table)


def binary_search(arr, start_idx, end_idx, target):
    if start_idx > end_idx:
        return start_idx

    mid_idx = (start_idx + end_idx) // 2
    mid_element = arr[mid_idx]

    if target == mid_element:
        return mid_element
    elif target < mid_element:
        return binary_search(arr, start_idx, mid_idx - 1, target)
    else:
        return binary_search(arr, mid_idx + 1, end_idx, target)


print(solution([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
# 6
