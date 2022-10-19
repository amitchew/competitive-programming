class Solution(object):
    def maxOperations(self, nums, k):
        x = defaultdict(int)
        i = 0 
        
        for num in nums:
            val = k - num
            
            if x[val] > 0:
                x[val] -= 1
                i += 1
            else:
                x[num] += 1
                
        return i 
