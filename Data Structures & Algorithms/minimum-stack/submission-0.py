class MinStack:

    def __init__(self):
        self.stack = [] # (curr_min, element)

    def push(self, val: int) -> None:
        if self.stack:
            curr_min = self.stack[-1][0]
            new_min  = min(val, curr_min)
            self.stack.append((new_min, val))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][1]
        

    def getMin(self) -> int:
        return self.stack[-1][0]
        
