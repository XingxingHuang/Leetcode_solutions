import timeit

class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        # too slow
        # mapping = {
        #         "0": "01",
        #         "1": "10"
        #     }
        # rows = ["0"]
        # for i in range(N-1):
        #     rows.append("".join([mapping[element] for element in rows[-1]]))
        # return int(rows[-1][K-1])
        # also slow
        # mapping = {
        #     "0": "1",
        #     "1": "0"
        # }
        # rows = ["0"]
        # for i in range(N-1):
        #     rows.append(rows[-1] + "".join([mapping[element] for element in rows[-1]]))
        # return int(rows[-1][K-1])
        # use recursive!
        if N == 1 and K == 1:
            return 0
        num_elements = 2**(N - 1)
        if K >  num_elements // 2:
            return 1 - self.kthGrammar(N-1, K - num_elements // 2)
        else:
            return self.kthGrammar(N-1,K)


def run():
    Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)
    print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))

if __name__ == '__main__':
    main()
