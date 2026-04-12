class MinStack:

    def __init__(self):
        self.x = []
        self.numStack = []
        self.mp = {}

    def push(self, val: int) -> None:
        self.x.append(val)
        self.mp[val] = self.mp.get(val, 0) + 1
        if (self.mp[val] == 1 and (len(self.numStack) == 0 or self.numStack[-1] > val)):
            self.numStack.append(val)
            
    def pop(self) -> None:
        self.mp[self.x[-1]] -= 1 
        if self.mp[self.x[-1]] == 0:
            self.mp.pop(self.x[-1])
        if self.numStack[-1] == self.x[-1] and self.mp.get(self.x[-1], 0) == 0:
            self.numStack.pop()
        self.x.pop()

    def top(self) -> int:
        return self.x[-1]

    def getMin(self) -> int:
        return self.numStack[-1]