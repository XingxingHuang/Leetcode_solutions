class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        # generates a string with ordered repeated char in T based on S and followed by chars in T but not in S
        # return "".join([s for s in S for t in range(T.count(s))] + [c for c in T if c not in S])
        # generates a string starting with chars in T but not in S, followed by ordered repeated char in T from on S
        return "".join(sorted(T, key = S.find))
