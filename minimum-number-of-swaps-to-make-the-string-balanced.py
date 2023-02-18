class Solution:
    def minSwaps(self, s: str) -> int:
        if len(s) == 0: return 0
        
        result = []

        for item in s:
            if item == '[': result.append(item)
            else:
                if result and result[-1] == '[': result.pop()
                else: result.append(item)
        
        return ceil(len(result)/4)
