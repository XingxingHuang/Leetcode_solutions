class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = 0
        while n != 0:
            bits += n % 2
            n = n // 2
        return bits