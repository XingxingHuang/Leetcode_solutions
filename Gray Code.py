class Solution:
    # @return a list of integers
    def grayCode(self, n):
        gray = [0]
        for i in xrange(0, n):
            gray += [(x + 2**i) for x in reversed(gray)]
        return gray
        
