# https://leetcode.com/problems/shortest-distance-to-a-character/description/


class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        l = [i for i, e in enumerate(S) if e == C]
        n = len(S)
        return [min(abs(i - ll) for ll in l) for i in range(n)]