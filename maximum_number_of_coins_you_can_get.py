class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        x = sorted(piles, reverse=True)
        result =0
        divided = len(piles)/3
        
        for i in range(len(piles)):
            if not divided : return result 
            if i%2 ==1:
                result +=x[i]
                divided -=1
