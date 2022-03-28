# implement stack using Queues

# using only two queues..
# should support 'push' 'top' pop' and empty

# only push to back, pop from front, size, is empty

import collections

class Mystack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    
    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0
        