class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        if target < matrix[0][0] or target > matrix[len(matrix)-1][len(matrix[0])-1]:
            return False

        def bisearch_row(begin, end):
            if begin == end:
                return begin
            middle = (begin+end) / 2
            if matrix[middle][0] == target or (matrix[middle][0] < target and matrix[middle+1][0] > target):
                return middle
            elif matrix[middle][0] > target:
                return bisearch_row(begin, middle-1)
            else:
                return bisearch_row(middle+1, end)

        row_idx = bisearch_row(0, len(matrix)-1)

        def bisearch_in_row(row, begin, end):
            if begin > end:
                return False
            if begin == end:
                return row[begin] == target 
            middle = (begin+end) / 2
            if row[middle] == target:
                return True
            elif row[middle] < target:
                return bisearch_in_row(row, middle+1, end)
            else:
                return bisearch_in_row(row, begin, middle-1)

        return bisearch_in_row(matrix[row_idx], 0, len(matrix[0])-1)

s = Solution()

inputs = [
    [[
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 3],
    [[
        [1],
        [3],
    ], 0],
    [
        [[1]], 1
    ],
    [[
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 13]
]

for i in inputs:
    print s.searchMatrix(*i)
