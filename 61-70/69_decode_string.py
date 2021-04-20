"""
Hi, here's your problem today. This problem was recently asked by Google:

Given a string with a certain rule: k[string] should be expanded to string k
times. So for example, 3[abc] should be expanded to abcabcabc.
Nested expansions can happen, so 2[a2[b]c] should be expanded to abbcabbc.

Your starting point:

def decodeString(s):
  # Fill this in.

print(decodeString('2[a2[b]c]'))
# abbcabbc
"""


def decodeString(s):
    _, decode = decodeStringHelper(s, 0, 1)
    return "".join(decode)


def decodeStringHelper(s, index, times):
    current_decode = []
    while index < len(s) and s[index] != "]":
        token = s[index]
        try:
            token = int(token)
            childIndex, childDecode = decodeStringHelper(s, index + 1, token)
            current_decode += childDecode
            index = childIndex
        except ValueError:
            if token == "[":
                pass
            else:
                current_decode.append(token)
        index += 1

    return index, current_decode * times


print(decodeString('2[a2[b]c]'))
# abbcabbc
