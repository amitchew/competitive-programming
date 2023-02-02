class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        results=[]
        counter={}
            

        for num in arr1:
             counter[num]=counter.get(num,0)+1
        
        for num in arr2:
            for i in range(counter[num]):
                results.append(num)
        for num in sorted(arr1):
            if num not in arr2:
                results.append(num)

        return (results)



    
