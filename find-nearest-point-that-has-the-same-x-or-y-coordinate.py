class Solution:
   def nearestValidPoint(self, x, y, points):
        ans=-1
        val=float('inf')
        for i in range(len(points)):
            a, b = points[i]
            if a==x or b==y:
                d = abs(a-x) + abs(b-y)
                if d < init_d:
                    val, ans = d, i
        return ans
