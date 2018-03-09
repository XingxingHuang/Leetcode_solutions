# https://leetcode.com/problems/min-stack/description/


class MinStack:
    """
        kind of slow since min need to be updated on both push and pop via a whole pass of list
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = list()
        self._min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._stack.append(x)
        if self._stack:
            self._min = min(self._stack)

    def pop(self):
        """
        :rtype: void
        """
        self._stack.pop()
        if self._stack:
            self._min = min(self._stack)

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self._min