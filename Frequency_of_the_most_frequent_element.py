class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        def check(check):
            for i in range(n):
                j = i + check - 1
                if j < n and nums[j] * check - (summ[j + 1] - summ[i]) <= k:
                    return True
            return False

        nums.sort()
        n = len(nums)
        summ = [0] + list(accumulate(nums))
        left, right = 1, n
        while left < right:
            mid = (left + right + 1) >> 1
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left
