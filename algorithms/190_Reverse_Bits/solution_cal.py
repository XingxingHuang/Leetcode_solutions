class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        bits = []
        while n != 0:
            bits.append(n % 2)
            n = n // 2
        bits += [0] * (32 - len(bits))
        for pos, num in enumerate(bits):
            result += num * 2**(31-pos)
        return result