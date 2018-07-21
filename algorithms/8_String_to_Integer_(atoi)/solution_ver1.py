class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str or not str.strip():
            return 0

        str = str.strip()

        sign = ''
        if str[0] in '+-':
            sign = str[0]
            str = str[1:]

        num = ''
        for i, c in enumerate(str):
            if c not in '0123456789':
                break
            else:
                num += c

        if not num:
            return 0

        final_num = int(sign + num)

        if (final_num < (-2 ** 31)):
            return -2 ** 31
        elif (final_num > (2 ** 31 - 1)):
            return 2 ** 31 - 1
        return final_num


