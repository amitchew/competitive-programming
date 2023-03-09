class DataStream:
    def __init__(self, value, k):
        
        self.answer = 0
        self.string = 0
        self.consecutive = 0

        self.answer = value
        self.string = 0
        self.consecutive = k

    def consec(self, num):

        if num == self.answer:
            self.string += 1

        else:
            self.string = 0

        if self.string>=self.consecutive:

            return True
        return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
