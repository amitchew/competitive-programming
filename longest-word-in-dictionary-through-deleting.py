class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary = sorted(dictionary, key=str.lower)
        dictionary = sorted(dictionary, key= lambda x: len(x), reverse=True)
        
        # Two pointers
        dic_s = Counter(s)
        
        for word in dictionary:
            dic_word = Counter(word)
            if not set(dic_word.keys()).issubset(set(dic_s.keys())):
                continue
            else:
                len_word = len(word)
                l, r = 0, 0
                while r < len(s):
                    if s[r] == word[l]:
                        l += 1
                    if l == len_word:
                        return word
                    r += 1
        return ""
