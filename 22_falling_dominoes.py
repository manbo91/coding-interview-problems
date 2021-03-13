"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given a string with the initial condition of dominoes, where:

. represents that the domino is standing still
L represents that the domino is falling to the left side
R represents that the domino is falling to the right side

Figure out the final position of the dominoes. If there are dominoes that get
pushed on both ends, the force cancels out and that domino remains upright.

Example:
Input:  ..R...L..R.
Output: ..RR.LL..RR
"""


class Solution(object):
    def pushDominoes(self, dominoes):
        dominoesList = list(dominoes)
        stack = list()

        idx = 0
        startIdx = idx
        while idx < len(dominoes):
            current_domino = dominoesList[idx]
            if current_domino == "L":
                if len(stack) > 0:
                    stack.pop()
                    left = startIdx
                    right = idx
                    while left < right:
                        if left == right:
                            break
                        dominoesList[left] = "R"
                        dominoesList[right] = "L"
                        left += 1
                        right -= 1
                else:
                    for j in range(startIdx, idx):
                        dominoesList[j] = "L"
                startIdx = idx
            elif current_domino == "R":
                stack.append(current_domino)
                startIdx = idx
            idx += 1
        if len(stack) > 0:
            for i in range(startIdx, len(dominoesList)):
                dominoesList[i] = "R"
        return "".join(dominoesList)


print(Solution().pushDominoes('..R...L..R.'))
# ..RR.LL..RR
print(Solution().pushDominoes('..R...L.....L..R......L..L..R....L..R..'))
# ..RR.LLLLLLLL..RRRRLLLLLLL..RRRLLL..RRR
