"""
solution using dynamic programming
"""
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self,s,dict):
        broke = {}
        for i in range(len(s)):
            if s[:i+1] in dict:
                broke[i] = True
            else:
                temp = False
                for j in range(i):
                    if broke[j] and s[j+1:i+1] in dict:
                        temp = True
                        break
                broke[i] = temp
        return broke[len(s)-1]



"""
initial recursion solution worked but slow

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self,s,dict):
        if s in dict:
            return True
        else:
            results = []
            for w in dict:
                if s.startswith(w):
                    results.append(self.wordBreak(s[len(w):],dict))
            if True in results:
                return True
            else:
                return False
"""
