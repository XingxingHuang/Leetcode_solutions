class Solution(object):
    def shiftingLetters(self, S, shifts):
        ans = []
        X = sum(shifts)
        for i, c in enumerate(S):
            ans.append(chr(ord('a') + (ord(c) - ord('a') + X) % 26))
            X = (X - shifts[i]) % 26
        return "".join(ans)