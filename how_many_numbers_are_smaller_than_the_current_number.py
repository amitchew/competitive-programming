class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        leng=len(nums)
        result=[]
        count=0
        for i in nums:
            for j in range(leng):
                if (nums[j]-i)<0:
                    count+=1
            result.append(count)
            count=0
        return result
