class Solution:
    # @return an integer
    def reverse(self, x):
        if x == 0: return 0
        else:
            positive = x > 0
            res = ""
            if positive:
                lst = [digit for digit in str(x)][::-1]
                for i in lst:
                    res += i
                return int(res)
            else:
                lst = [digit for digit in str(x)][1:][::-1]
                for i in lst:
                    res += i
                return -1*int(res)
