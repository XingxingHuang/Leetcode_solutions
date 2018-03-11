from collections import defaultdict
class Solution:
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        # time limit exceeded
        """
        scores = defaultdict(list)
        for i in range(len(A)):
            score = sum(map(lambda t: t[0] >= t[1], zip(range(len(A)), A[i:] + A[:i])))
            scores[score].append(i)
        return min(scores[max(scores.keys())])
