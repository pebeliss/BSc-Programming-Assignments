""""
An efficient data structure, Fliplist, which completes following operations in O(1) time:
    - Add an item to the end of the list
    - Add an item to the beginning of the list
    - Remove and return an item from the end of the list
    - Remove and return an item from the beginning of the list
    - Flip the entire list
"""

from collections import deque

class FlipList:
    def __init__(self):
        self.deque = deque()
        self.deque_rev = deque()
        self.first = None
        self.last = None
        self.first_rev = None
        self.last_rev = None
        self.rev = False
    
    """Add an item to the end of the list"""
    def push_last(self, x):
        if len(self.deque) == 0:
            self.first = x 
            self.last_rev = None
        self.deque.append(x)
        self.last = x
        self.deque_rev.appendleft(x)
        self.first_rev = x
    
    """Add an item to the beginning of the list"""
    def push_first(self, x):
        if len(self.deque) == 0:
            self.last = x
            self.first_rev = x
        self.deque.appendleft(x)
        self.first = x
        self.deque_rev.append(x)
        self.last_rev = x

    """Remove and return an item from the end of the list"""
    def pop_last(self):
        if len(self.deque) > 1:
            self.last = self.deque[-2]
            self.first_rev = self.deque_rev[1]
        else:
            self.last = self.deque[-1]
            self.first_rev = self.deque_rev[0]
        self.deque_rev.popleft()
        return self.deque.pop()

    """Remove and return an item from the beginning of the list"""
    def pop_first(self):
        if len(self.deque) > 1:
            self.first = self.deque[1]
            self.last_rev = self.deque_rev[-2]
        else:
            self.first = self.deque[0]
            self.last_rev = self.deque_rev[-1]
        self.deque_rev.pop()
        return self.deque.popleft()

    """Flip the entire list"""
    def flip(self):
        self.deque_rev, self.deque = self.deque, self.deque_rev

if __name__ == "__main__":
    f = FlipList()
    f.push_last(1)
    f.push_last(5)
    f.push_last(3)
    f.flip()
    print(f.pop_last()) # 1
    print(f.pop_last()) # 5
    print(f.pop_last()) # 3
