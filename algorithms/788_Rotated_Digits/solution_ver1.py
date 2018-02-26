# https://leetcode.com/problems/rotated-digits/description/

class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        # brute force O(NlogN)
        return sum(
            all(map(lambda digit: digit in '0125689', str(number))) and  # all digits are valid
            not all(map(lambda digit: digit in '018', str(number)))      # not all digits rotate to itself
            for number in range(1, N + 1)
            )


