

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return

        rows = len(matrix)
        cols = len(matrix[0])
        self.sum_arr = []

        for r in range(rows+1):
            self.sum_arr.append([0] * (cols+1))

        for r in range(rows):
            for c in range(cols):
                self.sum_arr[r+1][c+1] = self.sum_arr[r][c+1] + self.sum_arr[r+1][c] - self.sum_arr[r][c] + matrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum_arr[row2+1][col2+1] - self.sum_arr[row1][col2+1] - self.sum_arr[row2+1][col1] + self.sum_arr[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)