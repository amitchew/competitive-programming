class Solution: 
    def select(self, arr, i):
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]>arr[j]:arr[j],arr[i]=arr[i],arr[j]
        return arr
         
    
    def selectionSort(self, arr,n):
        for n in range(len(arr)):
            for j in range(n+1,len(arr)):
                if arr[n]>arr[j]:arr[j],arr[n]=arr[n],arr[j]
        return arr
