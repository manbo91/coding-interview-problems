"""
Hi, here's your problem today. This problem was recently asked by Amazon:

You are given an array of integers. Return the length of the longest consecutive
elements sequence in the array.

For example, the input array [100, 4, 200, 1, 3, 2] has the longest consecutive
sequence 1, 2, 3, 4, and thus, you should return its length, 4.

def longest_consecutive(nums):
  # Fill this in.

print(longest_consecutive([100, 4, 200, 1, 3, 2]))
# 4

Can you do this in linear time?
"""


def longest_consecutive(nums):
    nums_dict = {}
    for num in nums:
        nums_dict[num] = False

    max_count = 0
    for key, visited in nums_dict.items():
        if visited:
            continue

        current_count = 1

        next_key = key + 1
        while (next_key) in nums_dict:
            if nums_dict[next_key]:
                break
            current_count += 1
            next_key += 1

        prev_key = key - 1
        while (next_key) in nums_dict:
            if nums_dict[prev_key]:
                break
            current_count += 1
            prev_key -= 1

        max_count = max(current_count, max_count)

    return max_count


print(longest_consecutive([100, 4, 200, 1, 3, 2]))
# 4
