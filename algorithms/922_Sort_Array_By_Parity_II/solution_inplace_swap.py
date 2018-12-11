class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        curr = 0
        next_even = 0
        next_odd = 1
        while curr < len(A):
            if curr % 2 == 0:
                if A[curr] % 2 == 0:
                    next_even = max(next_even, curr + 2)
                    curr += 1
                else:
                    A[curr], A[next_odd] = A[next_odd], A[curr]
                    next_odd += 2
            elif curr % 2 == 1:
                if A[curr] % 2 == 1:
                    next_odd = max(next_odd, curr + 2)
                    curr += 1
                else:
                    A[curr], A[next_even] = A[next_even], A[curr]
                    next_even += 2
        return A
                    
                
                
        
