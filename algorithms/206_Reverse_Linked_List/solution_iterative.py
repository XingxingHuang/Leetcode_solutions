# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        prev = None
        curr = head
        while curr:
            temp_node = curr.next
            curr.next = prev
            prev = curr
            curr = temp_node
        return prev

