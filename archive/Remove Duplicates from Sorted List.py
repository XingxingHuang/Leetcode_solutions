# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            follower = current.next
            if current.val == follower.val:
                current.next = follower.next
            else:
                current = follower
        return head
