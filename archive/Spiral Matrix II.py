class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n == 0: return []
        if n == 1: return [[1]]
        # a list store all n^2 numbers
        number = [i+1 for i in range(n**2)]
        # initialize an matrix
        matrix = []
        for j in range(n):
            matrix.append([i for i in range(n)])
        # fill in the values layer by layer
        # keep track of current layer and current number
        k, layer, index = n, 0, 0
        while index < n**2:
            # top:
            for i in range(layer,k):
                matrix[layer][i] = number[index]
                index += 1
            # right
            for i in range(layer+1,k):
                matrix[i][k-1] = number[index]
                index += 1
            # bottom
            for i in range(1,k-layer):
                matrix[k-1][k-1-i] = number[index]
                index +=1
            # left
            for i in range(1,k-layer-1):
                matrix[k-1-i][layer] = number[index]
                index +=1
            # update indicators
            layer += 1
            k -= 1
        return matrix
                
if __name__ == "__main__":
    slt = Solution()
    for i in range(6):
        print i
        matrix = slt.generateMatrix(i)
        for j in matrix:
            print j
