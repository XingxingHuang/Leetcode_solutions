# https://leetcode.com/problems/find-and-replace-in-string/description/

class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        string comparison and operations
        """
        for i, s, t in sorted(zip(indexes, sources, targets), reverse=True):
            if S[i:i + len(s)] == s:
                S = S[:i] + t + S[i + len(s):]
        return S