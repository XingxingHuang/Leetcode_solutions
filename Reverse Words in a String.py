# Given an input string, reverse the string word by word.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".



class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        rs = ""
        if len(s.split()) == 0:
            return rs
        elif len(s.split()) == 1:
            return s.split()[0]
        else:
            words = s.split()
            reserved_words = words[::-1]
            for word in reserved_words:
                rs += word
            return rs[:-1]
            
