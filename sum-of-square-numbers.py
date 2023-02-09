class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l=0
        r=int(sqrt(c))
        if c<=2:
            return True
        
        while l<=r:
            k=(l*l) + (r*r) 
            if k==c:
                return True
            elif k<c:
                l=l+1
            else:
                r=r-1
        return False
