class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        return "".join([s for s in S for t in range(T.count(s))] + [c for c in T if c not in S])