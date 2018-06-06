#  https://leetcode.com/problems/reverse-integer/description/


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = int(self._reverse_string(str(x))) if x >= 0 else int('-' + self._reverse_string(str(x))[:-1])
        if result > 2147483648 or result < -2147483647:
            return 0
        return result

    def _reverse_string(self, s):
        l = len(s)
        if l < 2:
            return s
        return self._reverse_string(s[l // 2:]) + self._reverse_string(s[:l // 2])