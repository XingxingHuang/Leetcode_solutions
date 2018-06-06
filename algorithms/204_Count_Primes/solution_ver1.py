class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        initialize an array of indicators, assume everything is prime
        set 0 and 1 to not prime
        for a given number start from 2 to sqaure root of n plus 1
            starting from its square, and increment by the value of it self, mark all those as not Prime
        return the sum
        """
        if n < 2:
            return 0
        s = [1] * n
        s[0] = s[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if s[i] == 1:
                curr = 2 * i  # it is safe to change it to i * i, why????
                while curr < n:
                    s[curr] = 0
                    curr += i
        return sum(s)