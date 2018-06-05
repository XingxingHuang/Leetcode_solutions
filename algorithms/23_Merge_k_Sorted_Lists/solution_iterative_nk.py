# https://leetcode.com/problems/merge-k-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == []:
            return None
        curr = ListNode(0)
        dummy = curr
        lists = [node for node in lists if node is not None]
        while any(lists):
            min_val = min([node.val for node in lists])
            for idx, node in enumerate(lists):
                if node.val == min_val:
                    curr.next = ListNode(node.val)
                    curr = curr.next
                    lists[idx] = node.next
            lists = [node for node in lists if node is not None]
        return dummy.next