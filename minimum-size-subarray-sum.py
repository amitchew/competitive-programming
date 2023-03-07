class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        right_sum = 0 
        answer = None 

        for right in range(len(nums)):
       
            right_sum += nums[right]
                                    
            while right_sum >= target:
                                
                answer = min(answer or float('inf'), right + 1 - left)
            
                right_sum -= nums[left]
                left += 1

        return answer or 0
