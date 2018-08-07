# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def get_new_n(num):
            return sum([int(i) ** 2 for i in str(num)])

        if n == 1:
            return True

        nums_seen = set()

        while n != 1:
            new_n = get_new_n(n)
            if new_n in nums_seen:
                return False
            nums_seen.add(new_n)
            n = new_n
            print(n, new_n, nums_seen)

        return True

