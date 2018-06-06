class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        total = 0
        current = 0
        stack = []
        while current < len(height):
            while stack and height[current] > height[stack[-1]]:
                top = stack[-1]
                stack.pop()
                if not stack:
                    break
                distance = current - stack[-1] - 1
                bounded_height = min(height[current], height[stack[-1]]) - height[top]
                total += distance * bounded_height
            stack.append(current)
            current += 1
        return total