class Solution:
    def sortSentence(self, sentence: str) -> str:
        return ' '.join([i[:-1] for i in sorted(sentence.split(), key=lambda x:x[-1])])
