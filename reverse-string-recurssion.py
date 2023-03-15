class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s.reverse()
        begin=0
        end=len(s)-1

        self.reverse_string(begin,end,s)

    def reverse_string(self,begin,end,s):

        if begin<end:
            
            s[begin], s[end]=s[end],s[begin]

            begin+=1
            end-=1
            
            self.reverse_string(begin,end,s)



