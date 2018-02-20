# https://leetcode.com/problems/letter-case-permutation/description/
import timeit

class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        return list(self._permutation_generator(S))

    def _permutation_generator(self, S):
        if S == '':
            yield ''
            return
        for rest in self._permutation_generator(S[1:]):
            yield S[0].upper() + rest
            if S[0].upper() != S[0].lower():
                yield S[0].lower() + rest


def run():
    Solution().letterCasePermutation("a1b2")

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)

if __name__ == '__main__':
    main()
