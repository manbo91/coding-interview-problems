"""
Hi, here's your problem today. This problem was recently asked by AirBNB:

Given a list of words, group the words that are anagrams of each other.
(An anagram are words made up of the same letters).

Example:

Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]

Here's a starting point:

import collections

def groupAnagramWords(strs):
  # Fill this in.
"""


def groupAnagramWords(strs):
    group = {}
    for s in strs:
        key = "".join(sorted(s))
        group[key] = group.get(key, [])
        group[key].append(s)
    return [item for key, item in group.items()]


print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]
