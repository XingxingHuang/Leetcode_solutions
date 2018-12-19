class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        j = int(area ** 0.5)
        while area % j != 0:
            j -= 1
        return area // j , j

