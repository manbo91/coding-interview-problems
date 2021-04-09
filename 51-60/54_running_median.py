"""
Hi, here's your problem today. This problem was recently asked by Google:

You are given a stream of numbers. Compute the median for each new element.

Eg. Given [2, 1, 4, 7, 2, 0, 5], the algorithm should output
[2, 1.5, 2, 3.0, 2, 2, 2]

Here's a starting point:

def running_median(stream):
  # Fill this in.
"""


def running_median(stream):
    median = list()
    sorted_stream = []
    for i in range(len(stream)):
        sorted_stream.append(stream[i])
        sorted_stream.sort()
        size = len(sorted_stream)
        mid_index = size // 2
        if size % 2 == 0:
            value = (sorted_stream[mid_index - 1] +
                     sorted_stream[mid_index]) / 2
        else:
            value = sorted_stream[mid_index]
        median.append(value)
    return median


print(running_median([2, 1, 4, 7, 2, 0, 5]))
# 2 1.5 2 3.0 2. 2.0 2

import heapq


def running_median_second(stream):
    if len(stream) == 1:
        return stream[0]

    left_values = []
    right_values = [(stream[0], 0, stream[0])]
    medians = list()
    for i in range(1, len(stream)):
        size = len(left_values) + len(right_values)
        current_value = stream[i]

        left = None
        right = None
        if len(left_values) > 0:
            left = left_values[0][2]
        if len(right_values) > 0:
            right = right_values[0][2]

        if left is not None and right is not None:
            while len(right_values) > len(left_values):
                key, index, value = heapq.heappop(right_values)
                right = right_values[0][2]
                heapq.heappush(left_values, (-key, index, value))
            while len(right_values) < len(left_values):
                key, index, value = heapq.heappop(left_values)
                left = left_values[0][2]
                heapq.heappush(right_values, (-key, index, value))

        if current_value > right:
            heapq.heappush(right_values, (current_value, i, current_value))
        else:
            heapq.heappush(left_values, (-current_value, i, current_value))

        if size % 2 == 0:
            medians.append((left_values[0][2] + right_values[0][2]) / 2)
        else:
            medians.append(right_values[0][2])

    size = len(left_values) + len(right_values)
    if size % 2 == 0:
        medians.append((left_values[0][2] + right_values[0][2]) / 2)
    else:
        medians.append(right_values[0][2])
    return medians


print(running_median_second([2, 1, 4, 7, 2, 0, 5]))
# 2 1.5 2 3.0 2. 2.0 2
