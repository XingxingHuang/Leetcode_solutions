# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        bunny, turtle = head.next, head
        while bunny != turtle:
            if not bunny.next or not bunny.next.next:
                return False
            bunny = bunny.next.next
            turtle = turtle.next
        return True