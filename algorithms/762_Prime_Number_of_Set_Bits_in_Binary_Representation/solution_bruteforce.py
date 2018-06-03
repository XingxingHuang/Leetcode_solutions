# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/

class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        1. we don't need to write a prime calculation function,
           since L, R were constrained, and we can write out the possible primes easily

            2^10 = 1024
            so 10^6 < (2^10)^2 = 2^20
            --> we only need to worry about prime number < 20:
            2,3,5,7,11,13,17,19
        """
        POSSIBLE_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]
        # count = 0
        # for number in range(L, R + 1):
        #     # if sum([int(digit) for digit in bin(number)[2:]]) in POSSIBLE_PRIMES: # time limit exceed
        #     if bin(number).count('1') in POSSIBLE_PRIMES:
        #         count += 1
        # return count

        return sum(bin(number).count('1') in POSSIBLE_PRIMES for number in range(L, R + 1))