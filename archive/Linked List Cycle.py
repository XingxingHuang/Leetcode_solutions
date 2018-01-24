# Given a linked list, determine if it has a cycle in it.

# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# if there is a cycle in the linked list
# the fast runner will be trapped in the cycle
# while the slow runner will eventually enter the cycle
# before the slow runner finished one cycle the fast runner will meet it.

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        # initialize pointers
        # fast move two nodes in one iteration
        fast = head
        # slow move one node per iteration
        slow = head
        Cycle = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                Cycle = True
                break
        return Cycle