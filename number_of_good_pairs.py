class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pair={}
        result=0
        for num in nums:
            if not num in good_pair:
                good_pair[num]=0
            good_pair[num]+=1
        for num in good_pair:
            n=good_pair[num]
            result+=(n*(n-1)//2)
        return result
