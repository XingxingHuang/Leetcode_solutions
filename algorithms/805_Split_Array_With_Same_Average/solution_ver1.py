# https://leetcode.com/problems/split-array-with-same-average/description/


class Solution(object):
    """
        mean(B) = mean(C) implies that mean(B) = mean(A)
        if we normalize A (zero mean), then the problem reduce to whether we can find a subset which has mean 0
        To avoid checking all possible subsets, we can split the into two subset B and C, to have either some
        subset from either B or C with mean 0, or a subset from B, BB, and a subset from C, CC, resulting BB union CC
        has zero mean
    """
    def splitArraySameAverage(self, A):
        from fractions import Fraction
        N = len(A)
        S = sum(A)
        A = [z - Fraction(S, N) for z in A]

        if N == 1: return False

        #Want zero subset sum
        left = {A[0]}
        for i in range(1, N//2):
            left |= {z + A[i] for z in left}| {A[i]}
        if 0 in left: return True

        right = {A[-1]}
        for i in range(N//2, N-1):
            right |= {z + A[i] for z in right} | {A[i]}
        if 0 in right: return True

        sleft = sum(A[i] for i in range(N//2))
        sright = sum(A[i] for i in range(N//2, N))

        return any(-ha in right and (ha, -ha) != (sleft, sright) for ha in left)