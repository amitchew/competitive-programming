class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:


        counterr=Counter(p)
        result=[]
        window=Counter(s[:len(p)])
        rangee=len(s)-len(p)+1

        for i in range(rangee):
            if window==counterr:
                result.append(i)
                
            if i==len(s)-len(p):
                break

            window[s[i]]-=1
            if window[s[i]]==0:
                del window[s[i]]

            window[s[i+len(p)]]+=1
        return result

            


        

        




