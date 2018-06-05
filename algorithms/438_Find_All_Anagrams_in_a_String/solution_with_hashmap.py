def build_char_freq(p):
    char_freq = {}
    for char in p:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    return char_freq


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        keep a dictionary of current window
        update dictionary by remove the old head element and adding the new tail element counts
        remember to remove key
        """
        self._p_dict = build_char_freq(p)
        len_p = len(p)
        current_dict = build_char_freq(s[:len_p])
        rets = []
        if current_dict == self._p_dict:
            rets.append(0)
        for start in range(len(s) - len_p):
            current_dict[s[start]] -= 1
            if current_dict[s[start]] == 0:
                del current_dict[s[start]]
            if s[start + len_p] not in current_dict:
                current_dict[s[start + len_p]] = 1
            else:
                current_dict[s[start + len_p]] += 1
            if current_dict == self._p_dict:
                rets.append(start + 1)
        return rets
