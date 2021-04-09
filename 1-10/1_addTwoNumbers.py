# Input (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output 7 -> 0 -> 8
# Explanation: 342 + 465 = 807


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        output_list_head = None
        output_list_tail = None

        while l1 or l2 or c > 0:
            temp = 0

            if l1:
                temp += l1.val
                l1 = l1.next

            if l2:
                temp += l2.val
                l2 = l2.next

            temp += c
            remainder = temp % 10
            c = temp // 10

            if output_list_head is None:
                output_list_head = ListNode(remainder)
                output_list_tail = output_list_head
            else:
                output_list_tail.next = ListNode(remainder)
                output_list_tail = output_list_tail.next

        return output_list_head


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)

while result:
    print(result.val)
    result = result.next
