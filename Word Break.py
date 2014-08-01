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
