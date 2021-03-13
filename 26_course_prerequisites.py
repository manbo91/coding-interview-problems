"""
Hi, here's your problem today. This problem was recently asked by Google:

You are given a hash table where the key is a course code, and the value is a
list of all the course codes that are prerequisites for the key.
Return a valid ordering in which we can complete the courses.
If no such ordering exists, return NULL.

Example:
{
  'CSC300': ['CSC100', 'CSC200'],
  'CSC200': ['CSC100'],
  'CSC100': []
}

This input should return the order that we need to take these courses:
 ['CSC100', 'CSC200', 'CSCS300']
"""


def courses_to_take(course_to_prereqs):
    courses = [(course, len(course_to_prereqs[course]))
               for course in course_to_prereqs]
    courses.sort(key=lambda item: item[1])
    return [course[0] for course in courses]


courses = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}

print(courses_to_take(courses))
# ['CSC100', 'CSC200', 'CSC300']
