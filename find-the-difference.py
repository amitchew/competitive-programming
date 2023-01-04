class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        item = 0
        
        for i in range(len(s)):
            item += ord(t[i]) - ord(s[i])
        
        item += ord(t[-1])
                
        return chr(item)
