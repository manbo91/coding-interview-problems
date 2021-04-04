"""
i, here's your problem today. This problem was recently asked by Google:

You are given an array of tuples (start, end) representing time intervals
for lectures. The intervals may be overlapping. Return the number of rooms
that are required.

For example. [(30, 75), (0, 50), (60, 150)] should return 2.
"""


def solution(times):
    start_times = []
    end_times = []
    for time in times:
        start_time, end_time = time
        start_times.append(start_time)
        end_times.append(end_time)

    start_times.sort()
    end_times.sort()

    start_idx = 1
    end_idx = 0
    lecture_count = 1

    while start_idx < len(start_times) and end_idx < len(end_times):
        s_time = start_times[start_idx]
        e_time = end_times[end_idx]
        if s_time < e_time:
            lecture_count += 1
            start_idx += 1
        else:
            lecture_count -= 1
            end_idx += 1
    return lecture_count


print(solution([(30, 75), (0, 50), (60, 150)]))
# 2
