# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head :
            return head
        start = ListNode(312312312312)
        start.next = head
        front, sfront = head.next, head
        while front:
            back = start
            while back.next.val < front.val:
                back = back.next
            if back.next != front and back.next.val >= front.val:
                front.next, back.next, sfront.next = back.next, front, front.next
                front = sfront.next
            else:
                front, sfront.next = front.next, sfront.next
        return start.next
