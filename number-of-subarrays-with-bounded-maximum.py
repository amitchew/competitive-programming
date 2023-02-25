class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        end,start=-1,-1
        result=0

        for i in range(len(nums)):  
            if nums[i]>=left and nums[i]<=right:
                end=i
                result+=end-start

            elif nums[i]>right:
                start,end=i,i
                
            else:
                result+=end-start
                
        return result
