class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        def circle(row_begin, row_end, col_begin, col_end):
            if row_begin == row_end:
                for col in range(col_begin, col_end+1):
                    yield matrix[row_begin][col]
            elif col_begin == col_end:
                for row in range(row_begin, row_end+1):
                    yield matrix[row][col_begin]
            else:
                for col in range(col_begin, col_end):
                    yield matrix[row_begin][col]
                col += 1
                for row in range(row_begin, row_end):
                    yield matrix[row][col]
                row += 1
                for col in range(col_end, col_begin, -1):
                    yield matrix[row][col]
                col -= 1
                for row in range(row_end, row_begin, -1):
                    yield matrix[row][col]

        if not matrix:
            return []

        spiral = []
        row_begin = col_begin = 0
        row_end = len(matrix)-1
        col_end = len(matrix[0])-1

        while row_begin <= row_end and col_begin <= col_end:
            for elem in circle(row_begin, row_end, col_begin, col_end):
                spiral.append(elem)
            row_begin += 1
            row_end -= 1
            col_begin += 1
            col_end -= 1

        return spiral
