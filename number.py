"""
Object of class Number and its method .recursion() calculates how many ways
an integer between 1 and 50 can be represented as a sum of positive integers. 
The function pos_int_sum() gets the integer as its input, executes the class
Number and outputs the number of ways.
The function includes also sums consisting of only one integer.
"""

class Number:
    def __init__(self):
        self.counter = 0

    def recursion(self, n, m):
        if n == 0: 
            self.counter += 1
            return
        if m == 0 or n < 0:
            return 
        else:
            self.recursion(n, m-1)
            self.recursion(n-m, m)
    

def pos_int_sum(n):
    computation = Number()
    computation.recursion(n, n)
    return computation.counter

if __name__ == "__main__":
    print(pos_int_sum(4)) # 5
    print(pos_int_sum(5)) # 7
    print(pos_int_sum(8)) # 22
    print(pos_int_sum(42)) # 53174
