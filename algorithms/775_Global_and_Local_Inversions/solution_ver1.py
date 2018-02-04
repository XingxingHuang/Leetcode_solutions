# https://leetcode.com/problems/global-and-local-inversions/description/
import timeit

# all local inversion are global inversion
# if we see a global inversion that is not a local inversion then it is
# not an ideal permutation

class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        current_max = 0
        for i in range(len(A) - 2):
            current_max = max(current_max, A[i])
            if current_max > A[i + 2]:
                return False
        return True

def run():
    A = [1,2,3,4,6,8,0,5]
    Solution().isIdealPermutation(A)

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)

if __name__ == '__main__':
    main()
