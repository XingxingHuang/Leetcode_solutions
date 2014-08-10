# solution using binary search
class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self,x):
        lo, hi = 0, x/2+1
        mid = (lo+hi)/2
        while True:
            if mid**2 > x:          
                hi = mid
                mid = (lo+hi)/2
            elif mid**2 == x:
                return mid
                break
            elif (mid+1)**2 == x:
                return mid+1
                break
            elif (mid+1)**2 >x:
                return mid
                break
            else:
                lo = mid
                mid = (lo+hi)/2



"""
cheat solution actually much faster than solution above...

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        return int(x**0.5)
"""
