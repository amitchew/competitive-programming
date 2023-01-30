class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sorted_piles = sorted(piles)
        summ =0
        for i in range(len(piles)//3):
            summ += sorted_piles[(len(piles)-2)-(i*2)]
        return summ
