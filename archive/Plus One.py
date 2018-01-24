class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits): 
        number = int(''.join([str(x) for x in digits])) + 1
        return [int(x) for x in str(number)]
            
