class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.vals = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.vals.append(x)

        if self.min == None:
            self.min = x 
        elif x < self.min:
            self.min = x

    def pop(self):
        """
        :rtype: None
        """
        x = self.vals.pop()
        if x == self.min:
            self.min = self.recalculateMin()
        
        return x

    def top(self):
        """
        :rtype: int
        """
        x = self.vals.pop()
        self.vals.append(x)
        return x

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

    def recalculateMin(self):
        """
        :rtype: int
        """
        newMin = None

        for i in self.vals:
            if newMin == None:
                newMin = i
            elif i < newMin:
                newMin = i

        return newMin
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()