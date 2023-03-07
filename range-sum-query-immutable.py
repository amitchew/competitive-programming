class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum=[0]*(len(nums)+1)
        for i in range(len(nums)):
            self.prefix_sum[i+1]=self.prefix_sum[i] + nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        summ=self.prefix_sum[right+1] -self.prefix_sum[left]
        return summ


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
