class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        def digit_to_num(d):
            assert 64 <= ord(d) <= 90, 'FOUND A DIGIT {} WHICH IS NOT VALID'.format(d)
            return ord(d) - 64

        total = 0
        for loc, d in enumerate(s[::-1]):
            # print(loc, d, digit_to_num(d))
            total += digit_to_num(d) * 26 **(loc)
        return total


if __name__ == '__main__':
    print('A -> {}, expecting 1'.format(Solution().titleToNumber('A')))
    print('AB -> {}, expecting 28'.format(Solution().titleToNumber('AB')))
    print('ZY -> {}, expecting 701'.format(Solution().titleToNumber('ZY')))
