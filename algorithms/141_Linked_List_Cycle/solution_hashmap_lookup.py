# https://leetcode.com/problems/linked-list-cycle/description/

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
        nodes_seen = set()
        curr = head
        while curr:
            if curr not in nodes_seen:
                nodes_seen.add(curr)
                curr = curr.next
            else:
                return True
        return False
