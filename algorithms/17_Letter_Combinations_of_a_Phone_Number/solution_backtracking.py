# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution:
    digit_char_mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if digits == '':
            return []
        num_digits = len(digits)
        combos = []
        letters = ''
        self._backtracing(num_digits, combos, digits, letters, 0)
        return combos

    def _backtracing(self, num_digits, combos, digits, letters, current_digit_idx):
        if current_digit_idx == len(digits):
            combos.append(letters)
        else:
            for char in self.digit_char_mapping[digits[current_digit_idx]]:
                self._backtracing(num_digits, combos, digits, letters + char, current_digit_idx + 1)

