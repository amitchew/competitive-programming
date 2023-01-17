class Solution:
   def nearestValidPoint(self, x, y, points):
        init_d=float('inf')
        ans=-1
        for i in range(len(points)):
            a, b = points[i]
            if a==x or b==y:
                d = abs(a-x) + abs(b-y)
                if d < init_d:
                    init_d, ans = d, i
        return ans
