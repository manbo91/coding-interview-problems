"""
Hi, here's your problem today. This problem was recently asked by Apple:

Given a list of words, and an arbitrary alphabetical order, verify that the
words are in order of the alphabetical order.

Example:
Input:
words = ["abcd", "efgh"], order="zyxwvutsrqponmlkjihgfedcba"

Output: False
Explanation: 'e' comes before 'a' so 'efgh' should come before 'abcd'

Example 2:
Input:
words = ["zyx", "zyxw", "zyxwy"],
order="zyxwvutsrqponmlkjihgfedcba"

Output: True
Explanation: The words are in increasing alphabetical order

Here's a starting point:

def isSorted(words, order):
  # Fill this in.
"""


def compareCustomOrder(word1, word2, order):
    idx1 = 0
    idx2 = 0
    while idx1 < len(word1) and idx2 < len(word2):
        char1 = word1[idx1]
        char2 = word2[idx2]

        char1Idx = order.find(char1)
        char2Idx = order.find(char2)
        if char1Idx < char2Idx:
            return -1
        elif char1Idx > char2Idx:
            return 1
        else:
            idx1 += 1
            idx2 += 1

    if idx1 < len(word1):
        return 1
    if idx2 < len(word2):
        return -1
    return 0


def isSorted(words, order):
    for i in range(1, len(words)):
        comparison = compareCustomOrder(words[i - 1], words[i], order)
        if comparison == 1:
            return False
    return True


print(isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
# False
print(isSorted(["zyx", "zyxw", "zyxwy"], "zyxwvutsrqponmlkjihgfedcba"))
# True
