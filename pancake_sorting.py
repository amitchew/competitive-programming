class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans= []
        for item in range(len(arr),0,-1):
            index = arr.index(item)
            arr[:index+1]= arr[:index +1][::-1]
            arr[:item]= arr[:item][::-1]
            ans.append(index+1)
            ans.append(item)
        return ans 
