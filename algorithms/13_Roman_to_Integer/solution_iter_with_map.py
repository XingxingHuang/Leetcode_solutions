class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans_int_mapping = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        prev_val = 0
        running_total = 0
        n_digits = len(s)

        for i in range(n_digits):
            curr_val = romans_int_mapping[s[n_digits - i - 1]]
            running_total += curr_val if curr_val >= prev_val else - curr_val
            prev_val = curr_val

        return running_total