# create a class that supports operations
# must be O(1). difficult w/ tracking min
# to make O(1), keep track of mins on stack. when adding new
# element, if smaller than or equal to most recent min, then add onto.
    # adding even if equal to because we can have two of the same min, so
    # popping one does not remove it completely.
# when popping, if it is the most recent min, then remove from min stack.

class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins or val <= self.mins[-1]:
            self.mins.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.mins[-1]:
                self.mins.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.mins:
            return self.mins[-1]
        
