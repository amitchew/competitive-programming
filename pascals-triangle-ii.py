class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 2:
            return [1] * (rowIndex + 1)
        
        up_row = self.getRow(rowIndex - 1)
        
        current_row = [1] * (len(up_row) + 1)

        for i in range(1, len(current_row)-1):

            current_row[i] = up_row[i-1] + up_row[i]
        
        return current_row
