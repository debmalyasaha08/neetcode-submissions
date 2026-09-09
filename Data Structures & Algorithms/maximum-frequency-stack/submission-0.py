class FreqStack:

    def __init__(self):
        self.freq = {}
        self.group = {}
        self.maxFreq = 0

    def push(self, val: int) -> None:
        # Update frequency of the value
        f = self.freq.get(val, 0) + 1
        self.freq[val] = f
        
        # Update max frequency if necessary
        if f > self.maxFreq:
            self.maxFreq = f
            
        # Add the value to the list corresponding to its current frequency
        if f not in self.group:
            self.group[f] = []
        self.group[f].append(val)

    def pop(self) -> int:
        # Get the top element from the max frequency stack
        val = self.group[self.maxFreq].pop()
        
        # Decrement the frequency of the popped element
        self.freq[val] -= 1
        
        # If the max frequency list is empty, decrease maxFreq
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1
            
        return val

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()