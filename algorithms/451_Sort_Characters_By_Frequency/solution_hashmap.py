class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_freq = dict()
        for char in s:
            if char not in char_freq:
                char_freq[char] = 1
            else:
                char_freq[char] += 1
        sorted_chars = [(char, freq) for char, freq in char_freq.items()]
        sorted_chars.sort(key=lambda x: x[1], reverse=True)
        return "".join([char_freq[0] * char_freq[1] for char_freq in sorted_chars])
