class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.sum_arr = []
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        for _ in range(self.rows):
            self.sum_arr.append([0] * self.cols)

        for r in range(self.rows):
            for c in range(self.cols):
                if c == 0:
                    self.sum_arr[r][c] = matrix[r][c]
                else:
                    self.sum_arr[r][c] = self.sum_arr[r][c-1] + matrix[r][c]
            if r > 0:
                for c in range(self.cols):
                    self.sum_arr[r][c] += self.sum_arr[r-1][c]
            print(self.sum_arr[r])

    def update(self, row: int, col: int, val: int) -> None:
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        for r in range(row, self.rows):
            for c in range(col, self.cols):
                self.sum_arr[r][c] += delta

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0:
            if col1 == 0:
                return self.sum_arr[row2][col2]
            return self.sum_arr[row2][col2] - self.sum_arr[row2][col1-1]
        elif col1 == 0:
            return self.sum_arr[row2][col2] - self.sum_arr[row1-1][col2]
        return self.sum_arr[row2][col2] - self.sum_arr[row2][col1-1] - self.sum_arr[row1-1][col2] + self.sum_arr[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)