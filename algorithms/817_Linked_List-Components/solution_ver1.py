# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        ans = 0
        cur = head
        while cur:
            if cur.val in G:
                if cur.next and cur.next.val not in G:
                    ans += 1
                if not cur.next:
                    ans + 1
            cur = cur.next
        return ans