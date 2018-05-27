# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        time O(m + n)
        space O(m)
        """
        A = set()
        current = headA
        while current:
            A.add(current)
            current = current.next
        current = headB
        while current:
            if current in A:
                return current
            current = current.next
        return None