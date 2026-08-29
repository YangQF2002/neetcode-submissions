class MinStack:
    def __init__(self):
        self.stack = []

        # Define a min stack that tracks the minimum at each point in the stack 
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minStack) == 0:
            self.minStack.append(val)
        
        else: 
            # Look at the previous minimum (self.minStack[-1]) as well as the val
            # To determine the current minimum
            self.minStack.append(min(val, self.minStack[-1]))
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]

       