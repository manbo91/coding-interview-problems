"""
Hi, here's your problem today. This problem was recently asked by AirBNB:

Given two strings A and B of lowercase letters, return true if and only if
we can swap two letters in A so that the result equals B.

Example 1:
Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:
Input: A = "aa", B = "aa"
Output: true
Example 4:
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:
Input: A = "", B = "aa"
Output: false
Here's a starting point:

class Solution:
  def buddyStrings(self, A, B):
    # Fill this in.
"""


class Solution:
    def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False

        letter_set = set()
        diff_letter_index = list()
        for i in range(len(A)):
            letter_set.add(A[i])
            if A[i] != B[i]:
                diff_letter_index.append(i)
            if len(diff_letter_index) > 2:
                return False

        if len(letter_set) == 1:
            return True

        if len(diff_letter_index) == 2:
            i = diff_letter_index[0]
            j = diff_letter_index[1]
            newA = [x for x in A]
            newA[i], newA[j] = newA[j], newA[i]
            newA = "".join(newA)
            return newA == B

        return False


print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False
print(Solution().buddyStrings("ab", "ba"))
# Output: True
print(Solution().buddyStrings("ab", "ab"))
# Output: False
print(Solution().buddyStrings("abb", "bab"))
# Output: True
print(Solution().buddyStrings("aa", "aa"))
# Output: True
print(Solution().buddyStrings("aaaaaaabc", "aaaaaaacb"))
# Output: True
print(Solution().buddyStrings("", "aa"))
# Output: False
