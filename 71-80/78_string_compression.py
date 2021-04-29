"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given an array of characters with repeats, compress it in place.
The length after compression should be less than or equal to the original array.

Example:
Input: ['a', 'a', 'b', 'c', 'c', 'c']
Output: ['a', '2', 'b', 'c', '3']
Here's a starting point:

class Solution(object):
  def compress(self, chars):
    # Fill this in.

print Solution().compress(['a', 'a', 'b', 'c', 'c', 'c'])
# ['a', '2', 'b', 'c', '3']
"""


class Solution(object):
    def compress(self, chars):
        result = []
        currentChar = chars[0]
        count = 1
        for i in range(1, len(chars)):
            char = chars[i]
            if currentChar != char:
                result.append(currentChar)
                if count > 1:
                    result.append(count)
                currentChar = char
                count = 1
            else:
                count += 1
        result.append(currentChar)
        if count > 1:
            result.append(count)
        return result


print(Solution().compress(['a', 'a', 'b', 'c', 'c', 'c']))
# ['a', '2', 'b', 'c', '3']
