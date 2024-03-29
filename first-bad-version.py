# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        begin=1
        end=n

        while begin<end:
            middle=(begin+end)//2

            if isBadVersion(middle):
                end=middle

            else:
                begin=middle+1
            
        return begin

        
