import math
class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return round(math.log(1.0000001**a*1.0000001**b, 1.0000001))