class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        answer = 0
        stack = []
        const=(10 ** 9 + 7)
        arr.insert(0, -inf)  
        arr.append(-inf) 


        for i in range(len(arr)):

            while stack and arr[i] < arr[stack[-1]]:
                mid = stack.pop()
                left = mid - stack[-1]
                right = i - mid
                answer += left * right * arr[mid]

            stack.append(i)
        result=answer % const

        return result
