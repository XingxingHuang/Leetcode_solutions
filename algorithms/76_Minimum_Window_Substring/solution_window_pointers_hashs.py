class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not (set(t)).issubset(set(s)):
            return ""
        if len(s) < len(t):
            return ""

        chars_in_t = dict()
        for char in t:  # count the freq of chars in t
            chars_in_t[char] = chars_in_t.get(char, 0) + 1

        s_length = len(s)
        chars_to_match = len(set(t))
        chars_in_window = dict()
        window_l, window_r = 0, -1
        while chars_to_match > 0:
            window_r += 1  # move right pointer to the right
            if window_r >= s_length:  # scanned s once and couldn't even match all chars in t
                # break
                return ""
            current_char = s[window_r]
            chars_in_window[current_char] = chars_in_window.get(current_char, 0) + 1
            if current_char in chars_in_t and chars_in_window[current_char] == chars_in_t[current_char]:
                chars_to_match -= 1

        best_L, best_R = 0, window_r
        chars_in_window[s[window_r]] -= 1
        while window_l < window_r < s_length:
            chars_in_window[s[window_r]] = chars_in_window.get(s[window_r], 0) + 1
            # move window left pointer to the right, if left point char is not needed
            # stop when left pointer is at a char in t and the same time the window can not be shrunkened anymore atm
            while s[window_l] not in chars_in_t or chars_in_window[s[window_l]] > chars_in_t[s[window_l]]:
                chars_in_window[s[window_l]] -= 1
                window_l += 1

            if window_r - window_l < best_R - best_L:  # current_window is smaller than best so far
                best_L, best_R = window_l, window_r

            window_r += 1

        return s[best_L: best_R + 1]