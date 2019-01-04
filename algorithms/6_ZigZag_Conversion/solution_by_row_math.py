class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        if numRows == 2:
            return s[::2] + s[1::2]
        max_gap = 2 * (numRows - 1)
        ans = ""
        for row in range(numRows):
            if row >= len(s):
                break
            gap, alt_gap = max_gap - 2 * row, 2 * row
            if alt_gap == 0:
                ans += s[row::gap]
            elif gap == 0:
                ans += s[row::alt_gap]
            else:
                loc = row
                step = 0
                ans += s[row]
                while loc < len(s):
                    if step == 0:
                        loc += gap
                        step = 1
                    else:
                        loc += alt_gap
                        step -= 1
                    if loc < len(s):
                        ans += s[loc]
            # print(row, ans)
        return ans
