class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.temp_matrix=matrix
        for i in range(len(matrix)):
            for j in range(1,len(matrix[0])):
                self.temp_matrix[i][j]+=self.temp_matrix[i][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        summ=0
        if col1==0:
            for i in range(row1,row2+1):
                summ+=self.temp_matrix[i][col2]
        else:

            for i in range(row1,row2+1):
                summ+=(self.temp_matrix[i][col2] - self.temp_matrix[i][col1-1])
        return summ
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
