class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        resul = ""
        i = j = 0
        while i < len(word1) and j < len(word2):
            if word1[i:] > word2[j:]:
                resul += word1[i]
                i += 1
            else:
                resul += word2[j]
                j += 1 
        return resul+word1[i:]+word2[j:]
