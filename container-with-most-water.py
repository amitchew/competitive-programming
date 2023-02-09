class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxim = 0 
        l = 0
        r = len(height)-1
        while l < r:
            horiz = abs(l-r)
            area = horiz * min(height[l],height[r])
            maxim = max(area,maxim)
            if height[l] > height[r]:
                r -=1
            else:
                l +=1
        return maxim 
