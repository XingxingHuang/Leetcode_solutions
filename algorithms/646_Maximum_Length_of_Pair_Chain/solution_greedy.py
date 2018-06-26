class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        b, ans = float('-inf'), 0
        for c, d in sorted(pairs, key = lambda x: x[1]):
        # for c, d in sorted(pairs, key = operator.itemgetter(1)):
            if b < c:
                b = d
                ans += 1
        return ans