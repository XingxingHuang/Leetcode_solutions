class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        w, h = p, q
        if w == h:
            return 1
        while True:
            w += p
            h += q
            if w % p == 0 and h % (2 * p) == 0:
                return 0
            if w % (2 * p) == 0 and (h - p) % (2 * p) == 0:
                return 2
            if (w - p) % (2 * p) == 0 and (h - p) % (2 * p) == 0:
                return 1

