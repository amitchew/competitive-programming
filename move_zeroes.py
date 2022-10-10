class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j=0
        for digits in nums:
            if digits!=0:
                nums[j]=digits
                j +=1
        for i in range (j,len(nums)):
            nums[i]=0
