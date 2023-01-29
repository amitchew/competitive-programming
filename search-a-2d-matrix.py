class Solution:
    def searchMatrix(self, matrix, target):
        l = 0 
        r = len(matrix)
        for i in range(len(matrix)):
            if matrix[i][len(matrix[i])-1] >= target:
                break
        l,r = 0 , len(matrix[i])-1
        while l <= r:
            m = (l+r)//2
            if matrix[i][m] > target:
                r = m-1
            elif matrix[i][m] < target:
                l = m+1
            else:
                 return True
        return False
