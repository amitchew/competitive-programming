class Solution:
    def similarPairs(self, words: List[str]) -> int:
        cnt= defaultdict(int)
        for w in words:
            s=[0 for _ in range(26)]
            for ch in w:
                s[ord(ch) - ord('a')]=1
            cnt[tuple(s)] +=1
        res = sum(i*(i-1)//2 for i in cnt.values())
        return res
