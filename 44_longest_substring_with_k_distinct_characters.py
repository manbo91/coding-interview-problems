"""
Hi, here's your problem today. This problem was recently asked by Amazon:

You are given a string s, and an integer k. Return the length of the longest
substring in s that contains at most k distinct characters.

For instance, given the string:
aabcdefff and k = 3, then the longest substring with 3 distinct characters
would be defff. The answer should be 5.

Here's a starting point:

def longest_substring_with_k_distinct_characters(s, k):
  # Fill this in.
"""


def longest_substring_with_k_distinct_characters(s, k):
    if len(s) <= k:
        return len(s)

    longest = 0
    char_dict = dict()
    char_dict[s[0]] = 0
    start_index = 0
    for i in range(1, len(s)):
        char = s[i]
        char_dict[char] = char_dict.get(char, i)
        longest = max(i - start_index + 1, longest)
        if len(char_dict) > k:
            del_key = None
            prev_min_val = float('inf')
            min_val = float('inf')
            for key, value in char_dict.items():
                if value < min_val:
                    del_key = key
                    prev_min_val = min_val
                    min_val = value
            del char_dict[del_key]
            start_index = prev_min_val

    return longest


print(longest_substring_with_k_distinct_characters('aabcdefff', 3))
# 5 (because 'defff' has length 5 with 3 characters)
print(longest_substring_with_k_distinct_characters('aabacdaefaff', 3))
# 6 (because 'aefaff' has length 5 with 3 characters)
