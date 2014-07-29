class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        sums = [(i+1,j+1) for i in range(len(num)) for j in range(i+1,len(num)) if num[i]+num[j] == target]
        return sums[0][0],sums[0][1]
