"""
Given a string, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        longest = 0
        start_index = 0
        chars = {}
        for i, char in enumerate(s):
            if char in chars:
                if start_index <= chars[char]:
                    longest = max(i - start_index, longest)
                    start_index = chars[char] + 1

            chars[char] = i

        longest = max(len(s) - start_index, longest)

        return longest

    def substringOfLongestSubstring(self, s):
        longest = 0
        longest_start_index = 0
        longest_end_index = 0
        start_index = 0
        chars = {}
        for i, char in enumerate(s):
            if char in chars:
                if start_index <= chars[char]:
                    current_length = i - start_index

                    if current_length > longest:
                        longest = current_length
                        longest_start_index = start_index
                        longest_end_index = i

                    start_index = chars[char] + 1

            chars[char] = i

        last_current_length = len(s) - start_index
        if last_current_length > longest:
            longest = last_current_length
            longest_start_index = start_index
            longest_end_index = len(s) - 1

        return s[longest_start_index:longest_end_index]


print(Solution().lengthOfLongestSubstring("abrkaabcdefghijjxxx"))
print(Solution().substringOfLongestSubstring("abrkaabcdefghijjxxx"))
print(Solution().lengthOfLongestSubstring("aaaba"))
print(Solution().substringOfLongestSubstring("aaaba"))
