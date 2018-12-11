class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        n = 0
        for chars in zip(*A):
            if list(chars) != sorted(chars):
                n += 1
        return n
