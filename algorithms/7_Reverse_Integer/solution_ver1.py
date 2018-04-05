#  https://leetcode.com/problems/reverse-integer/description/


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = int(str(x)[::-1]) if x >= 0 else int('-' + str(x)[1:][::-1])
        if result > 2147483648 or result < -2147483647:
            return 0
        return result
