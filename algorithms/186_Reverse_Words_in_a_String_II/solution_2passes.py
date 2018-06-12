class Solution(object):
    def reverse(self, str, start, end):
        """
                a i r b n b
        start + 0 1 2 3 4 5 == end
        0 + 5 = 1 + 4 = 2 + 3
        i   j
        """
        n = end - start + 1
        for i in range(start, start + n // 2):
            j = start + end - i
            str[i], str[j] = str[j], str[i]
        return str

    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        b l u e _ a p r o n
                ||
        n o r p a _ e u l b
        |       |
      start    end
                ||
        a p r o n _ e u l b
                    |     |
                  start  end
                ||
        a p r o n _ b l u e
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