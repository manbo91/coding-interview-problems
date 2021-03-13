"""
This problem was recently asked by Twitter.
"""
"""
A palindrome is a sequence of characters that reads the same backwards
and forwards. Given a string, s, find the longest palindromic substring in s.
"""
"""
Example:
Input: "banana"
Output: "anana"

Input: "million"
Output: "illi"
"""


class Solution:
    def longestPalindrome(self, s):
        longestSubstringStartIdx = 0
        longestSubstringEndIdx = 0
        longestLength = 0

        for i in range(1, len(s) - 1):
            # Case 1 even
            evenLength = 0
            leftIdx = i
            rightIdx = i + 1
            while leftIdx > 0 and rightIdx < len(s):
                if s[leftIdx] == s[rightIdx]:
                    evenLength += 2
                    leftIdx -= 1
                    rightIdx += 1
                else:
                    break

            if evenLength > longestLength:
                longestLength = evenLength
                longestSubstringStartIdx = leftIdx + 1
                longestSubstringEndIdx = rightIdx

            # Case 2 odd
            oddLength = 1
            leftIdx = i - 1
            rightIdx = i + 1
            while leftIdx > 0 and rightIdx < len(s):
                if s[leftIdx] == s[rightIdx]:
                    oddLength += 2
                    leftIdx -= 1
                    rightIdx += 1
                else:
                    break

            if oddLength > longestLength:
                longestLength = oddLength
                longestSubstringStartIdx = leftIdx + 1
                longestSubstringEndIdx = rightIdx

        return s[longestSubstringStartIdx:longestSubstringEndIdx]


s = "tracecars"
print(str(Solution().longestPalindrome(s)))
s = "banana"
print(str(Solution().longestPalindrome(s)))
s = "million"
print(str(Solution().longestPalindrome(s)))
