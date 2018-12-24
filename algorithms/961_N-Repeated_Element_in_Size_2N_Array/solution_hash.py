class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        value_counts = dict()
        for element in A:
            value_counts[element] = value_counts.get(element, 0) + 1
            if value_counts[element] > 1:
                break
        return element
