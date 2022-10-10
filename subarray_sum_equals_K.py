class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefix=0
        count = Counter({0:1})
        for num in nums:
            prefix += num
            result += count[prefix-k]
            count[prefix] +=1
        return result 
