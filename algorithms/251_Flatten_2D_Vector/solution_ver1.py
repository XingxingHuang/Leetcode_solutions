class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = [li for li in vec2d if li != []]
        self.n = len(self.vec2d)
        self.li = None
        self.el = None

        i = 0
        while i < self.n:
            if len(self.vec2d[i]) != 0:
                self.li = i
                self.el = 0
                break
            i += 1

    def next(self):
        """
        :rtype: int
        """
        if self.li < self.n - 1:
            val = self.vec2d[self.li][self.el]
            if self.el < len(self.vec2d[self.li]) - 1:
                self.el += 1
            else:
                self.li += 1
                self.el = 0
        else:
            val = self.vec2d[self.li][self.el]
            if self.el <= len(self.vec2d[self.li]) - 1:
                self.el += 1
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.li is None or self.el is None:
            return False
        if self.li < self.n - 1:
            return True
        elif self.el <= len(self.vec2d[self.li]) - 1:
            return True
        return False

    # Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())