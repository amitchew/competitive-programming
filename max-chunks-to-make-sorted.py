class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res=0
        ans=0
        for i in range (len(arr)):
            if arr[i]>res:
                res=arr[i]
            if res==i:
                ans+=1
        return ans
        
