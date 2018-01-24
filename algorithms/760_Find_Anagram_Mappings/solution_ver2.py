# https://leetcode.com/problems/find-anagram-mappings/description/
import timeit

class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        mapping = {val: idx for idx, val in enumerate(B)}
        return [mapping[val] for val in A]

def run():
    A = [12, 28, 46, 32, 50]
    B = [50, 12, 32, 46, 28]
    Solution().anagramMappings(A, B)

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)

if __name__ == '__main__':
    main()
