"""
This data structure gets an integer between 1 and 10^9 as its input and returns
the smallest mode of the numbers that have already been added to the data structure.
An object of this class can be given up to 10^5 integers.
"""

class Mode:
    def __init__(self):
        self.modes = {}
        self.max_value = 0
        self.min_key = 10**9
    
    """The add method performs both the integer adding and returning the smallest mode."""
    def add(self, x):
        if x in self.modes:
            self.modes[x] += 1
        else:
            self.modes[x] = 1
        
        if self.max_value < self.modes[x]:
            self.max_value = self.modes[x]
            self.min_key = x
        
        elif self.max_value == self.modes[x]:
            if x < self.min_key:
                self.min_key = x
            
        return self.min_key

if __name__ == "__main__":
    m = Mode()
    print(m.add(1)) # 1
    print(m.add(2)) # 1
    print(m.add(2)) # 2
    print(m.add(1)) # 1
    print(m.add(3)) # 1
    print(m.add(3)) # 1
    print(m.add(3)) # 3
    
