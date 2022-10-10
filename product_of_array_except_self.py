class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = len(nums)
        prefix = [1] * x 
        suffix = [1] * x
        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in reversed(range(x-1)):
            suffix[i] = suffix[i+1] * nums[i+1]
        return [ prefix[i]*suffix[i] for i in range(x) ]
