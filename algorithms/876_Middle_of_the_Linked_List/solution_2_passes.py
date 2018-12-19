# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import math


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 1
        node = head
        while node.next:
            length += 1
            node = node.next
        for i in range(int(math.ceil(length / 2))):
            head = head.next
        return head
