class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
	# if we alwasy put the min/max at the left most location
	# it reduce to a problem of size - 1, with min or max shiftted by 1
        minimum = 0
        maximum = len(S)
        result = []
        for idx, s in enumerate(S):
            if s == 'I':
                result.append(minimum)
                minimum += 1
            else:
                result.append(maximum)
                maximum -= 1
        result.append(minimum)
        return result
