class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len=len(s1)
        s2_len=len(s2)

        temp_dic_1=Counter(s1)
        temp_dic_2=Counter(s2[:s1_len-1])
        temp=0
        
        for i in range(s1_len-1,s2_len):
            temp_dic_2[s2[i]]+=1
            if temp_dic_1==temp_dic_2:
                return True

            temp_dic_2[s2[temp]]-=1

            if temp_dic_2[s2[temp]]==0:
                del temp_dic_2[s2[temp]]
            temp+=1

        return False
