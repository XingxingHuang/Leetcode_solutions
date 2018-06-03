# https://leetcode.com/problems/integer-to-english-words/description/


class Solution:
    oneToNineteen = [
        '', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven',
        'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
    ]
    tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

    def toWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return []
        if num < 20:
            return [self.oneToNineteen[num]]
        if num < 100:  # 20 ~ 99
            return [self.tens[num // 10]] + self.toWords(num % 10)
        if num < 1000:  # 100 ~ 999
            return [self.oneToNineteen[num // 100]] + ['Hundred'] + self.toWords(num % 100)
        for power, unit in enumerate(['Thousand', 'Million', 'Billion']):
            if num < 1000 ** (power + 2):
                return self.toWords(num // 1000 ** (power + 1)) + [unit] + self.toWords(num % 1000 ** (power + 1))

    def numberToWords(self, num):
        return ' '.join(self.toWords(num)).strip() or 'Zero'