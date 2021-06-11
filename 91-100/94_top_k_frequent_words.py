"""
Hi, here's your problem today. This problem was recently asked by AirBNB:

Given a non-empty list of words, return the k most frequent words. The output should be sorted from highest to lowest frequency, and if two words have the same frequency, the word with lower alphabetical order comes first. Input will contain only lower-case letters.

Example:
Input: ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"], k = 2
Output: ["pro", "daily"]

class Solution(object):
  def topKFrequent(self, words, k):
    # Fill this in.
"""

class Solution(object):
  def topKFrequent(self, words, k):
    answer = []
    wordCount = {}
    for word in words:
      wordCount[word] = wordCount.get(word, 0) + 1
      if wordCount[word] == k:
        answer.append(word)

    answer.sort(reverse=True)
    return answer

words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']
k = 1
print(Solution().topKFrequent(words, k))
# ['problems', 'pro', 'interview', 'for', 'daily']
k = 3
print(Solution().topKFrequent(words, k))
# ['pro']


