class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        begin=0
        end=len(nums)-1

        while begin<=end:
            middle=(end+begin)//2

            if nums[middle]<target:
                begin=middle+1

            elif nums[middle]>target:
                end=middle-1

            else:
                return middle     
        return (end+1)
