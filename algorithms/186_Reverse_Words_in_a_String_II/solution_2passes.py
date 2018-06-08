class Solution(object):
    def reverse(self, str, start, end):
        n = end - start + 1
        for i in range(start, start + n // 2):
            j = end - (i - start)
            str[i], str[j] = str[j], str[i]
        return str

    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        n = len(str)
        self.reverse(str, 0, n - 1)
        start = end = 0
        for i in range(n):
            if str[i] == ' ':
                self.reverse(str, start, end)
                start = end = i + 1
            else:
                end = i
        if start < end:
            self.reverse(str, start, end)