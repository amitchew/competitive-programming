class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed=[]
        for i in range(len(matrix[0])):
            n=[]
            for j in range(len(matrix)):
                n.append(matrix[j][i])
            transposed.append(n)
        return transposed
