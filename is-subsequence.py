class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x=0
        y=0
        if len(s)==0: return True
        
        while x<len(s) and y<len(t):
            if s[x]==t[y]:
                x+=1
            y+=1
        
        if x==len(s): return True
        return False
