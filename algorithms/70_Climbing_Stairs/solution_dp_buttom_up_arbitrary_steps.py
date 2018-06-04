class Solution:
    def climbStairs(self, n, step_sizes = (1,2)):
        """
        :type n: int
        :type step_sizes: iterable
        :rtype: int
        # watch out the upper boundary in the loop
        """
        if n == 0:
            return 1
        ways = [1]
        for remaining_steps in range(1, n + 1):
            total_ways = 0
            for step_size in step_sizes:
                if remaining_steps - step_size >= 0:
                    total_ways += ways[remaining_steps - step_size]
            ways.append(total_ways)
        return ways[-1]


