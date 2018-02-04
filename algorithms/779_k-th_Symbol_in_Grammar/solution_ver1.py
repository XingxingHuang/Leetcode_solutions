import timeit

class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        # use recursive!
        if N == 1 and K == 1:
            return 0
        num_elements = 2**(N - 1)
        if K >  num_elements // 2:
            return 1 - self.kthGrammar(N-1, K - num_elements // 2)
        else:
            return self.kthGrammar(N-1,K)


def run():
    Solution().kthGrammar(4,5)

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)

if __name__ == '__main__':
    main()
