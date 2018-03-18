class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        brute force
        """
        digits = [str(i) for i in range(10)] + ['a', 'b', 'c', 'd', 'e', 'f']
        results = {
            (int(r*2, 16) - int(color[1:3], 16))**2 + \
            (int(g*2, 16) - int(color[3:5], 16))**2 + \
            (int(b*2, 16) - int(color[5:7], 16))**2 : (r,g,b)
            for r in digits for g in digits for b in digits}
        r,g,b = results[min(results.keys())]
        return '#' + r + g + b