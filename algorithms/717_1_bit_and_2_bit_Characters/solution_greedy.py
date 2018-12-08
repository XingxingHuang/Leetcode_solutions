class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        while bits:
            if bits == [0]:
                return True
            bits = bits[1:] if bits[0] == 0 else bits[2:]
        return False
