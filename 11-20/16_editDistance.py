"""
Hi, here's your problem today. This problem was recently asked by AirBNB:

Given two strings, determine the edit distance between them.
The edit distance is defined as the minimum number of edits
(insertion, deletion, or substitution) needed to change one string to the other.

For example, "biting" and "sitting" have an edit distance of 2
(substitute b for s, and insert a t).
"""


def distance(s1, s2):
    change_count = 0

    idx_1 = 0
    idx_2 = 0
    while idx_1 < len(s1) - 1 and idx_2 < len(s2) - 1:
        if s1[idx_1] == s2[idx_2]:
            idx_1 += 1
            idx_2 += 1

        else:
            # substitution
            if s1[idx_1 + 1] == s2[idx_2 + 1]:
                idx_1 += 1
                idx_2 += 1
            # deletion
            elif s1[idx_1 + 1] == s2[idx_2]:
                idx_1 += 1
            # insertion
            elif s1[idx_1] == s2[idx_2 + 1]:
                idx_2 += 1

            change_count += 1

    while idx_1 < len(s1) - 1:
        idx_1 += 1
        change_count += 1

    while idx_2 < len(s2) - 1:
        idx_2 += 1
        change_count += 1

    return change_count


print(distance('biting', 'sitting'))
# 2
print(distance('abcdefg', 'abcg'))
# 3
