class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        (a_real + a_img i) *  (b_real + b_img i) = ...
        just expand the terms
        """
        a_real, a_img = [int(x) for x in a.replace('i','').split('+')]
        b_real, b_img = [int(x) for x in b.replace('i','').split('+')]
        return str(a_real * b_real - a_img * b_img)+'+'+str(a_real * b_img + a_img * b_real)+'i'