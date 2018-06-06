# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# reverseList is directly copied from 206. Reverse Linked List
# find the middle point
# reverse the second half
# compare the first half with the second half
# be nice and re do the reverse of the second half before return

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

    def _get_midpoint(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        mid = self._get_midpoint(head)
        rev = self.reverseList(mid)
        p, q = head, rev
        while p and q and p != q:
            if p.val != q.val:
                self.reverseList(mid)
                return False
            else:
                p = p.next
                q = q.next
        self.reverseList(mid)
        return True