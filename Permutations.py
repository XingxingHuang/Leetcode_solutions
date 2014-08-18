class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if len(num) == 1: return [num]
        if len(num) == 2: return [num,[num[1],num[0]]]
        results = []
        for i in xrange(len(num)):
            result = self.permute(num[:i]+num[i+1:])
            results.extend([[num[i]] + j for j in result])
        return results
