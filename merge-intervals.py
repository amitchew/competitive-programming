class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result=[]
        for item in sorted(intervals):
            if not result or result[-1][1]< item[0]:
                result.append(item)
            else:
                result[-1][1]= max(result[-1][1], item[1])
        return result
