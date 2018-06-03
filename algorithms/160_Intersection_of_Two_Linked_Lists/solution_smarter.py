# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        [a][ c ][ b][ c ]
        [ b][ c ][a][ c ]
        when concate linked list b to the end of a, linkied list a to the end of b
        align them together -> if they intersect, then the start of the intersection
        will be perfectly aligned in the second half

        time : O(m + n)
        space: O(1)
        """
        AtoB, BtoA = False, False
        currentA, currentB = headA, headB
        while currentA and currentB:
            if currentA == currentB:
                return currentA
            if not currentA.next and not AtoB:
                currentA = headB
                AtoB = True
            else:
                currentA = currentA.next
            if not currentB.next and not BtoA:
                currentB = headA
                BtoA = True
            else:
                currentB = currentB.next
        return None

