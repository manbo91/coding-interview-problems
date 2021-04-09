"""
Hi, here's your problem today. This problem was recently asked by Twitter:

You are given an array of k sorted singly linked lists. Merge the linked lists
into a single sorted linked list and return it.

Here's your starting point:

class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    c = self
    answer = ""
    while c:
      answer += str(c.val) if c.val else ""
      c = c.next
    return answer

def merge(lists):
  # Fill this in.
"""


class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer


def merge(lists):
    output_list_head = None
    output_list_tail = None

    list_head_dict = {i: head for i, head in enumerate(lists)}
    while len(list_head_dict) > 0:
        min_value = float('inf')
        min_key = None

        for key in list_head_dict:
            head = list_head_dict[key]
            if head.val < min_value:
                min_value = head.val
                min_key = key

        if min_key is not None:
            if output_list_head is None:
                output_list_head = list_head_dict[min_key]
                output_list_tail = output_list_head
            else:
                output_list_tail.next = list_head_dict[min_key]
                output_list_tail = output_list_tail.next

            list_head_dict[min_key] = list_head_dict[min_key].next
            if list_head_dict[min_key] is None:
                del list_head_dict[min_key]

    return output_list_head


a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print(merge([a, b]))
# 123456
