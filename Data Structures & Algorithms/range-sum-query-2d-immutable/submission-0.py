# O(1) complexity, must precompute w/ prefix sum

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                self.sumMat[r + 1][c + 1] = prefix + self.sumMat[r][c + 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sumBottomRight = self.sumMat[row2 + 1][col2 + 1]

        firstRect = self.sumMat[row1][col2 + 1]
        secondRect = self.sumMat[row2 + 1][col1]

        overlap = self.sumMat[row1][col1]

        return sumBottomRight - firstRect - secondRect + overlap
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)