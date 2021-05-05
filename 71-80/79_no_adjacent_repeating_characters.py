"""
Hi, here's your problem today. This problem was recently asked by LinkedIn:

Given a string, rearrange the string so that no character next to each other
are the same. If no such arrangement is possible, then return None.

Example:
Input: abbccc
Output: cbcbca
def rearrangeString(s):
  # Fill this in.

print rearrangeString('abbccc')
# cbcabc
"""

import heapq


def rearrangeString(s):
    pq = [(-s.count(x), x) for x in set(s)]
    heapq.heapify(pq)

    if any(-nc > (len(s) + 1) / 2 for nc, x in pq):
        return None

    ans = []
    while len(pq) >= 2:
        nct1, ch1 = heapq.heappop(pq)
        nct2, ch2 = heapq.heappop(pq)
        ans.extend([ch1, ch2])
        if nct1 + 1: heapq.heappush(pq, (nct1 + 1, ch1))
        if nct2 + 1: heapq.heappush(pq, (nct2 + 1, ch2))

    return "".join(ans) + (pq[0][1] if pq else '')


print(rearrangeString('abbccc'))
# cbcabc
print(rearrangeString('aabbccc'))
# cabcabc
print(rearrangeString('aslfjalksdjfqwenrjaas'))
# ajasafjlsadefjklnqrsw
print(rearrangeString('aaaaa'))
# None
print(rearrangeString('aabaa'))
# None
print(rearrangeString('aaaab'))
# None
print(rearrangeString('baaaa'))
# None
print(rearrangeString('ab'))
# ab
print(rearrangeString('aba'))
# aba
print(rearrangeString('abc'))
# abc
print(rearrangeString('abcabc'))
# abcabc
