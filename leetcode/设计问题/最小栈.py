class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l=[]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x in None:
            pass
        else:
            self.l.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.l) !=0:
            return 'error'

        self.l.remove(self.l[-1])


    def top(self):
        """
        :rtype: int
        """
        if len(self.l) !=0:
            return 'error'

        return self.l[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.l) !=0:
            return 'error'

        return min(self.l)
