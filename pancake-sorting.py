class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        out= []
        for i in range(len(arr),0,-1):
            index = arr.index(i)
            arr[:index+1]= arr[:index +1][::-1]
            arr[:i]= arr[:i][::-1]
            out.append(index+1)
            out.append(i)
        return out 
