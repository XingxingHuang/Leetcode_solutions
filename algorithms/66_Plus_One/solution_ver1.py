# https://leetcode.com/problems/plus-one/description/

class Solution:
    def plusOne(self, digits):
        return [int(i) for i in str(int(''.join([str(i) for i in digits])) + 1)]