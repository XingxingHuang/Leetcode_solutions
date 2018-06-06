# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n <= 0:
            return head
        if not head.next:
            return None
        start = ListNode(0)
        start.next = head
        left = start
        right = start
        for i in range(n):
            right = right.next

        while right.next:
            left = left.next
            right = right.next

        left.next = left.next.next
        return start.next
