class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.instack = []
        self.outstack = []
        self.front = None

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if not self.instack:
            self.front = x
        self.instack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while self.instack:
            self.outstack.append(self.instack.pop())

        ret = self.outstack.pop()
        self.front = self.outstack[-1] if self.outstack else None

        while self.outstack:
            self.instack.append(self.outstack.pop())

        return ret

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.front

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.instack



        # Your MyQueue object will be instantiated and called as such:
        # obj = MyQueue()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.peek()
        # param_4 = obj.empty()