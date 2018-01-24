class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        n1,n2 = 0,0
        for i in range(len(num1)):
            n1 += 10**i*int(num1[-i-1])
        for i in range(len(num2)):
            n2 += 10**i*int(num2[-i-1])
        return str(n1*n2)



"""
class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        return str(int(num1)*int(num2))
"""
