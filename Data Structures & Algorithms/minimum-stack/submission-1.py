class MinStack:

    def __init__(self):
        self.stack = []
    def push(self, val: int) -> None:
        min_val = 0
        if self.stack:
            min_val = min(val, self.stack[-1][1])
        else:
            min_val = val
        self.stack.append((val, min_val))
        

    def pop(self) -> None:
        if self.stack:
            del self.stack[-1]
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        
