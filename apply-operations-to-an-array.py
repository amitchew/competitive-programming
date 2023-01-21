class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0

        nonZero = [x for x in nums if x != 0] 
        zeroes = [j for j in nums if j == 0] 
        return( nonZero + zeroes) 
    
