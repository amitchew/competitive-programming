class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        sett = {}
        if len(words) < 2:
            return True
        
        for item, char in enumerate(order):
            sett[char] = item
        
        def compareInput(str1: str, str2: str) -> bool:
            item = 0
            while(item<len(str1) and item<len(str2)):
                order1 = sett[str1[item]]
                order2 = sett[str2[item]]
                item += 1
                if( order1 > order2 ):
                    return False 
                elif ( order1 < order2 ):
                    return True
            if item < len(str1): 
                return False
            
            return True
        
        for item in range(len(words)-1):
            if not compareInput(words[item], words[item+1]):
                return False
        return True
