class MyQueue:

    def __init__(self):
        self._stack_1 = []
        self._stack_2 = []
        self._length = 0

    def push(self, x: int) -> None:
        self._stack_1.append(x)
        self._length += 1
        return None

    def pop(self) -> int:
        if self._stack_2:
            self._length -= 1
            return self._stack_2.pop()
        else:
            while self._stack_1:
                self._stack_2.append(self._stack_1.pop())
            if self._stack_2:
                self._length -= 1
                return self._stack_2.pop()
            else:
                raise Exception()

    def peek(self) -> int:
        if self._stack_2:
            return self._stack_2[-1]
        else:
            while self._stack_1:
                self._stack_2.append(self._stack_1.pop())
            if self._stack_2:
                return self._stack_2[-1]
            else:
                raise Exception()

    def empty(self) -> bool:
        return not bool(self._length)
