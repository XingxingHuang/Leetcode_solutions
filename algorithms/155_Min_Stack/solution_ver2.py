# https://leetcode.com/problems/min-stack/description/

class MinStack(object):
    """
        use tuple to store (val, min)
        trade space for speed
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = list()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._stack.append((x, min([val for val in [self.getMin(), x] if val is not None])))

    def pop(self):
        """
        :rtype: void
        """
        self._stack.pop() if self._stack else None

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1][0] if self._stack else None


    def getMin(self):
        """
        :rtype: int
        """
        return self._stack[-1][1] if self._stack else None