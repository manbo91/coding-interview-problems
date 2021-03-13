"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

You are given an array of intervals - that is, an array of tuples (start, end).
The array may not be sorted, and could contain overlapping intervals.
Return another array where the overlapping intervals are merged.

For example:
[(1, 3), (5, 8), (4, 10), (20, 25)]

This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and (4, 10)
can be merged into (4, 10).
"""


def merge(intervals):
    intervals.sort(key=lambda item: item[0])

    new_intervals = list()
    current_start, current_end = intervals[0]
    for i in range(1, len(intervals)):
        start, end = intervals[i]

        if start > current_end:
            new_intervals.append((current_start, current_end))
            current_start = start
            current_end = end
            continue

        else:
            current_start = min(start, current_start)
            current_end = max(end, current_end)

    new_intervals.append((current_start, current_end))
    return new_intervals


print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
# [(1, 3), (4, 10), (20, 25)]
