class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        import math
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        h = [0] * cols
        left = [-1] * cols
        right = [cols] * cols

        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == '1':
                    h[col] = h[col] + 1
                else:
                    h[col] = 0

            last_col = -1
            for col in range(cols):
                if matrix[row][col] == '1':
                    left[col] = max(left[col], last_col)
                else:
                    left[col] = -1
                    last_col = col

            last_col = cols
            for col in range(cols-1, -1, -1):
                if matrix[row][col] == '1':
                    right[col] = min(right[col], last_col)
                else:
                    right[col] = cols
                    last_col = col

            for col in range(cols):
                max_area = max(max_area, math.pow(min(h[col], (right[col]-left[col]-1)), 2))

        return max_area
