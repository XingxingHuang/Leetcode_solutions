class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        res = [[]]
        S.sort()
        for e in S:
            res += [l+[e] for l in res]
        return res
