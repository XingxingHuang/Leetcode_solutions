class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if sum(gas)<sum(cost): 
            return -1
        elif len(gas)==1:
            return 0
        else:
            remains = [gas[0]-cost[0]]
            for i in xrange(1,len(gas)):
                remains.append(remains[i-1]+gas[i]-cost[i])
            reverse = remains[::-1]
            return len(gas)-reverse.index(min(remains))
