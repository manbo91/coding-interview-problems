"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

Given a time in the format of hour and minute, calculate the angle of the
hour and minute hand on a clock.

def calcAngle(h, m):
  # Fill this in.
"""


def calcAngle(h, m):
    oneHourAngle = 360 / 12
    oneMinAngle = 360 / 60

    minAngle = m * oneMinAngle
    hourAngle = h * oneHourAngle if h != 12 else 0

    percent = m / 60
    hourAngle += 5 * percent * oneMinAngle

    return minAngle - hourAngle if minAngle > hourAngle else hourAngle - minAngle


print(calcAngle(3, 30))
# 75
print(calcAngle(12, 30))
# 165
