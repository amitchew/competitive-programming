class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
      
        frequency_max = 0
        lenght_max = 0
        start = end = 0
        temp = defaultdict(int)
        while end < len(s):

            temp[s[end]] += 1
            frequency_max = max(frequency_max, temp[s[end]])
            
            
            if ((end-start+1) - frequency_max) > k:
                temp[s[start]] -= 1
                start += 1
                
            else:
                lenght_max = max(lenght_max, end-start+1)
            end += 1
        return lenght_max
