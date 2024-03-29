class Solution:
    def findKthBit(self, n: int, k: int) -> str:
  
        def answer(n, k):
            if n == 1:
                return "0"
        
            ans = answer(n-1, k)
            final = ""

            for a in ans:
                if a == "1":
                    final+="0"
                else:
                    final+="1"                   
            ans  = ans + "1" + final[::-1]
            return ans
        final_ans = answer(n, k)
        return final_ans[k-1]
