class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        assert 1 <= len(A) <= 50000, 'invalid input array length'
        if len(A) == 1:
            return True

        sign = 'equal'
        prev = A[0]
        for curr in A[1:]:
            if curr == prev:
                continue
            elif curr > prev:
                if sign == 'less':
                    return False
                else:
                    sign = 'greater'
            else:
                if sign == 'greater':
                    return False
                else:
                    sign = 'less'
            prev = curr
        return True