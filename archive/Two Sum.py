"""
accepted solution O(n)
iterate through the list once
"""
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict = {}
        for i, n in enumerate(num):
            if target-n in dict:
                return (dict[target-n]+1,i+1)
            else:
                dict[n] = i
"""
initial solution O(n^2) 


class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        sums = [(i+1,j+1) for i in range(len(num)) for j in range(i+1,len(num)) if num[i]+num[j] == target]
        return sums[0]

"""
