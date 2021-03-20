"""
Hi, here's your problem today. This problem was recently asked by Google:

A look-and-say sequence is defined as the integer sequence beginning with
a single digit in which the next term is obtained by describing the previous
term. An example is easier to understand:

Each consecutive value describes the prior value.

1      #
11     # one 1's
21     # two 1's
1211   # one 2, and one 1.
111221 # #one 1, one 2, and two 1's.

Your task is, return the nth term of this sequence.
"""


def nth_sequence(n):
    sequence = nth_sequence_recursive(1, n, ["1"])
    return "".join(sequence)


def nth_sequence_recursive(n, target, sequence):
    if n == target:
        return sequence

    new_sequence = []
    i = 1
    while (i < len(sequence)):
        prev_digit = sequence[i - 1]
        digit = sequence[i]

        if prev_digit == digit:
            new_sequence.append("2")
            new_sequence.append(digit)
            i += 1
        else:
            new_sequence.append("1")
            new_sequence.append(prev_digit)
            new_sequence.append("1")
            new_sequence.append(digit)
            i = i + 2

    # if sequence ["1"]
    if len(new_sequence) == 0:
        new_sequence = ["1", "1"]
    return nth_sequence_recursive(n + 1, target, new_sequence)


print(nth_sequence(1))  # 1
print(nth_sequence(2))  # 11
print(nth_sequence(3))  # 21
print(nth_sequence(4))  # 1211
print(nth_sequence(5))  # 111221
