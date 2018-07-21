class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'

        curr_str = '1'
        next_str = ''
        for i in range(1, n):
            while curr_str:
                cnt, c = self.scan(curr_str)
                next_str += '{}{}'.format(cnt, c)
                curr_str = curr_str[cnt:]
            curr_str = next_str
            next_str = ''
        return curr_str

    def scan(self, s):
        if len(s) == 1:
            return 1, s[0]
        if s == '':
            return 0, ''

        c = s[0]
        cnt = 1
        loc = 1
        while loc < len(s):
            if s[loc] != c:
                break
            else:
                cnt += 1
                loc += 1
        return cnt, c
