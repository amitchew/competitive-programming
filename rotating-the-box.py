class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m ,n= len(box),len(box[0])
        no_val = '.'
        stone = '#'
        obstacle = '*'
        result = [[no_val for _ in range(m)] for _ in range(n)]

        def write_stones (i, j, stones):
            for r in range(j, j - stones, -1):
                result[r][m-i-1] = stone

        for i in range(m):
            j, k = n-1, n-1
            stones = 0
            while k >= -1:
                if k == -1:
                    write_stones(i, j, stones)
                    break
                    
                if box[i][k] == obstacle:
                    write_stones(i, j, stones)
                    result[k][m-i-1] = obstacle

                    stones = 0
                    j = k - 1
                elif box[i][k] == stone:
                    stones += 1

                k -= 1

        return result
