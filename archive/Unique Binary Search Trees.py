class Solution:
    # @return an integer
    def numTrees(self, n):
        if n == 0: return 0
        elif n == 1: return 1
        elif n == 2: return 2
        else:
            num = 0
            for i in range(n):
                if i == 0 or i == n-1:
                    num += self.numTrees(n-1)
                else:                
                    num += self.numTrees(i) * self.numTrees(n-1-i)
            return num