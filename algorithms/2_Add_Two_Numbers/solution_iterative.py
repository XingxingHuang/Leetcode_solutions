# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        use an indicator variable to carry over the overflowing 1 to next digit calculation
        """
        result = ListNode(42)
        carry = 0
        current = result
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            if val >= 10:
                val -= 10
                carry = 1
            else:
                carry = 0
            current.next = ListNode(val)
            current = current.next
        if carry == 1:
            current.next = ListNode(1)
        return result.next