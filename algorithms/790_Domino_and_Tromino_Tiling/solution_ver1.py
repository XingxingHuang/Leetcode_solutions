# https://leetcode.com/problems/domino-and-tromino-tiling/description/

class Solution:
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        # much faster than dp, how to prof and could i find this pattern out if on whiteboard?
        s = [1, 2, 5]
        ans = 1
        if N < 3:
            ans = s[N - 1]
        else:
            for i in range(3, N):
                s.append(2 * s[i - 1] + s[i - 3])
            ans = s[-1]
        return ans % (10 ** 9 + 7)

