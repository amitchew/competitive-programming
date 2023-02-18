class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        arr1 = sorted(nums1)[::-1]
        arr2 = sorted([num, i] for i, num in enumerate(nums2))[::-1]
	
        ans = [-1 for x in range(n)]
        start, end = 0, n-1
    
        for num, i in arr2:
            if arr1[start] > num:
                ans[i] = arr1[start]
                start += 1
            else:
                ans[i] = arr1[end]
                end -= 1
    
        return ans
