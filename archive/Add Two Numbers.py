# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        carry = 0
        current = result
        while l1 or l2:
            s = carry
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            if s >= 10:
                s -= 10
                carry = 1
            else:
                carry = 0
            current.next = ListNode(s)
            current = current.next
        if carry == 1:
            current.next = ListNode(1)
        return result.next
