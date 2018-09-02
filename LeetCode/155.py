class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        return

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack += [x]
        return

    def pop(self):
        """
        :rtype: void
        """
        if not self.stack:
            return None
        self.stack.pop()
        return

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return min(self.stack)



        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()