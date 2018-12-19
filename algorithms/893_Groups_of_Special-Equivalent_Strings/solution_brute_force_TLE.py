class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def _special_equivalent(S, T):
            if len(S) != len(T):
                return False
            return sorted(S[1::2]) == sorted(T[1::2]) and sorted(S[::2]) == sorted(T[::2])
        groups = []


        while A:
            S = A.pop()
            group = [S]
            for T in A:
                if _special_equivalent(S,T):
                    group.append(T)
            A = [i for i in A if i not in group]
            groups.append(group)
        return len(groups)
