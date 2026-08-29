class MinStack:
    def __init__(self):
        self.structure = []
        self.prevMins = []
        self.freq = {}

        # Since question implies that this stack deals with integer elements
        self.currMin = None 
        
    def push(self, val: int) -> None:
        self.structure.append(val)
        if self.freq.get(val) is None: 
            self.freq.update({val : 1})
        else: 
            self.freq[val] += 1

        if self.currMin is None:
            self.currMin = val

        if val < self.currMin: 
            self.prevMins.append(self.currMin)
            self.currMin = val

    def pop(self) -> None:
        removedValue = self.top()
        self.freq[removedValue] -= 1
        self.structure.pop()

        print(self.freq)
        if removedValue == self.currMin and self.freq[removedValue] == 0: 
            if self.prevMins: 
                self.currMin = self.prevMins.pop()
            else: 
                self.currMin = None 
       

    def top(self) -> int:
        return self.structure[-1]
        
    def getMin(self) -> int:
        return self.currMin 



