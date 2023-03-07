class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer=[]

        current_sum=0

        for i in range(len(nums)):
            answer.append(current_sum+nums[i])
            current_sum=answer[i]
        return answer
