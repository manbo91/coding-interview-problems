"""
Hi, here's your problem today. This problem was recently asked by Amazon:

You are given an array of integers, and an integer K. Return the subarray which
sums to K. You can assume that a solution will always exist.

def find_continuous_k(list, k):
  # Fill this in.

print(find_continuous_k([1, 3, 2, 5, 7, 2], 14))
# [2, 5, 7]

Can you do this in linear time?
"""


def find_continuous_k(list, k):
    start_idx = 0
    idx = 0
    current_sum = 0
    while idx < len(list):
        if current_sum == k:
            return list[start_idx:idx]

        if current_sum > k:
            current_sum -= list[start_idx]
            start_idx += 1
            continue

        current_sum += list[idx]
        idx += 1
    return None


print(find_continuous_k([1, 3, 2, 5, 7, 2], 14))
# [2, 5, 7]
