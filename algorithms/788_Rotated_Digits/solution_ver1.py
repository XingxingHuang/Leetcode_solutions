class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        total = 0
        rotate_change = ['2', '5', '6', '9']
        rotate_unchange = ['0', '1', '8']
        for number in range(1, N + 1):
            if all(map(lambda digit: digit in rotate_change + rotate_unchange, str(number))):
                if not all(map(lambda digit: digit in rotate_unchange, str(number))):
                    total += 1
        return total


