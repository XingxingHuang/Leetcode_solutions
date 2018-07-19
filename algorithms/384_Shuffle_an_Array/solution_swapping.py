class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.length = len(nums)
        self.initial = list(nums)
        self.array = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.array = [i for i in self.initial]
        return self.array

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(self.length):
            new_loc = random.randint(0, self.length - 1)
            self.array[i], self.array[new_loc] = self.array[new_loc], self.array[i]

        return self.array

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()