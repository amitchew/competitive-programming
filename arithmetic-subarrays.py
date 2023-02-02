class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            res.append(self.checkCurrentSubarray(nums[l[i]:r[i]+1]))
        return res
    
    def checkCurrentSubarray(self, arithmetic):
        
        arithmetic.sort()
        difference = arithmetic[1] - arithmetic[0]
        for j in range(2, len(arithmetic)):
            if arithmetic[j] - arithmetic[j-1] != difference:
                return False
        return True
