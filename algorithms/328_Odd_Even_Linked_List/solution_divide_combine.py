# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        even = ListNode(-9999)
        even_start = even

        odd = ListNode(-9999)
        odd_start = odd

        current_odd = True

        while head:
            if current_odd:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next

            head = head.next
            current_odd = not current_odd

        even.next = None
        odd.next = even_start.next
        return odd_start.next