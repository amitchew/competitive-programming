class MyCircularQueue:

    def __init__(self, k: int):
        self.circular_queue=[0]*k
        self.q_length=0

        self.rear=0
        self.front=0
        

    def enQueue(self, value: int) -> bool:

        if self.isFull():
            return False
      
        self.circular_queue[self.rear]=value

        self.rear=(self.rear+1)%len(self.circular_queue)
        self.q_length+=1

        return True


    def deQueue(self) -> bool:

        if self.isEmpty():
            return False

        self.front=(self.front+1)%len(self.circular_queue)
        self.q_length-=1
        return True
        

    def Front(self) -> int:
        return self.circular_queue[self.front] if not self.isEmpty() else -1
        

    def Rear(self) -> int:
        return self.circular_queue[self.rear-1] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        if self.q_length==0:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if self.q_length==len(self.circular_queue):
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
