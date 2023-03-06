class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        k_sum=sum(nums[:k])

        average_k=k_sum/k
        result=average_k
        
        for i in range(len(nums)-k):
            k_sum-=nums[i]
            k_sum+=nums[i+k]
            average_k=k_sum/k
            result=max(result,average_k)
        return result
