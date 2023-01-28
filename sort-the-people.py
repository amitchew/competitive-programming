class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        temp=[]
        for item in range(len(heights)):
            temp.append([heights[item],names[item]])
        temp.sort(reverse=True)
        res=[]
        for item in temp:
            res.append(item[1])
        return res
