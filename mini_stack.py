class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, num: int) -> None:
        minimum_no = num if not self.stack else min(self.stack[-1][1], num)
        self.stack.append([num, minimum_no])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
