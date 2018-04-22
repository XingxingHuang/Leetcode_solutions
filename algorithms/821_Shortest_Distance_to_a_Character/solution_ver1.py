class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        l = [i for i, e in enumerate(S) if e == C]
        return [min(abs(i - ll) for ll in l) for i in range(len(S))]