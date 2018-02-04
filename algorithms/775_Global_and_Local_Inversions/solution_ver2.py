# https://leetcode.com/problems/global-and-local-inversions/description/
import timeit

# all local inversion are global inversion
# if we see a global inversion that is not a local inversion then it is
# not an ideal permutation
# Since this is a permutation from 1 to N
# the ith element should not be more than 2 away from it's position index

class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return all(abs(i - v) <= 1 for i, v in enumerate(A))

def run():
    A = [1,2,3,4,6,8,0,5]
    Solution().isIdealPermutation(A)

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)

if __name__ == '__main__':
    main()
