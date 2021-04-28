"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given a Roman numeral, find the corresponding decimal value. Inputs will
be between 1 and 3999.

Example:
Input: IX
Output: 9

Input: VII
Output: 7

Input: MCMIV
Output: 1904
Roman numerals are based on the following symbols:
I     1
IV    4
V     5
IX    9
X     10
XL    40
L     50
XC    90
C     100
CD    400
D     500
CM    900
M     1000
Numbers are strings of these symbols in descending order. In some cases,
subtractive notation is used to avoid repeated characters. The rules are as
follows:

1.) I placed before V or X is one less,
so 4 = IV (one less than 5), and 9 is IX (one less than 10)

2.) X placed before L or C indicates ten less,
so 40 is XL (10 less than 50) and 90 is XC (10 less than 100).

3.) C placed before D or M indicates 100 less,
so 400 is CD (100 less than 500), and 900 is CM (100 less than 1000).

class Solution():
  def romanToInt(self, s):
    # Fill this in.

n = 'MCMX'
print(Solution().romanToInt(n))
# 1910
"""


class Solution():
    def romanToInt(self, s):
        result = 0

        index = 0
        while (index < len(s)):
            current_char = s[index]

            if current_char == "M":
                result += 1000
                index += 1
                continue

            if current_char == "C":
                index += 1
                if index == len(s):
                    result += 100
                    break
                next_char = s[index]
                if next_char == "M":
                    result += 900
                    index += 1
                elif next_char == "D":
                    result += 400
                    index += 1
                else:
                    result += 100
                continue

            if current_char == "D":
                result += 500
                index += 1
                continue

            if current_char == "X":
                index += 1
                if index == len(s):
                    result += 10
                    break
                next_char = s[index]
                if next_char == "C":
                    result += 90
                    index += 1
                elif next_char == "L":
                    result += 40
                    index += 1
                else:
                    result += 10
                continue

            if current_char == "L":
                result += 50
                index += 1
                continue

            if current_char == "I":
                index += 1
                if index == len(s):
                    result += 1
                    break
                next_char = s[index]
                if next_char == "X":
                    result += 9
                    index += 1
                elif next_char == "V":
                    result += 4
                    index += 1
                else:
                    result += 1

            if current_char == "V":
                result += 5
                index += 1
                continue

        return result

    def romanToInt2(self, s):
        LETTER = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        number = 0
        lastVal = 0
        for i in range(len(s) - 1, -1, -1):
            currentVal = LETTER[s[i]]

            if currentVal >= lastVal:
                number += currentVal
            else:
                number -= currentVal

            lastVal = currentVal

        return number


n = 'MCMX'
print(Solution().romanToInt(n))
# 1910
print(Solution().romanToInt2(n))
# 1910
