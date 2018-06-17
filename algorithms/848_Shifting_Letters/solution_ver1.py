class Solution:
    chars = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    mapping = {k: v for k, v in zip(chars, range(len(chars)))}
    reverse_mapping = {v: k for k, v in zip(chars, range(len(chars)))}

    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        return "".join([self.shift_a_char(char, n) for char, n in zip(S, self.cumsum(shifts))])

    def shift_a_char(self, char, n):
        char_idx = self.mapping[char]
        new_idx = (char_idx + n) % 26
        return self.reverse_mapping[new_idx]

    def cumsum(self, shifts):
        shifts = shifts[::-1]
        for i in range(1, len(shifts)):
            shifts[i] += shifts[i - 1]
        return shifts[::-1]