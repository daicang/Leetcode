class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # New coordinate: (row, col) -> (col, n-row)

        half = n / 2
        if n % 2 == 1:
            col_range = half + 1
        else:
            col_range = half

        for row in range(half):
            for col in range(col_range):
                last = matrix[row][col]
                last_r = row
                last_c = col
                for _ in range(4):
                    r = last_c
                    c = n - 1 - last_r
                    matrix[r][c], last = last, matrix[r][c]
                    last_r = r
                    last_c = c

        return matrix


inputs = [
    # [[1,2,3],[4,5,6],[7,8,9]],
    [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],
]

def print_arr(arr):
    for row in arr:
        print ' '.join(['{:>2}'.format(n) for n in row])
    print '\n'

s = Solution()
for input in inputs:
    print_arr(input)
    ans = s.rotate(input)
    print_arr(ans)

    print '\n'
