class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])

        clear_r0 = False
        clear_c0 = False

        for r in range(rows):
            if matrix[r][0] == 0:
                clear_c0 = True
                break
        for c in range(cols):
            if matrix[0][c] == 0:
                clear_r0 = True
                break

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    print 'mark row %s col %s' % (r, c)
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, rows):
            if matrix[r][0] == 0:
                print 'clear row %s' % r
                for c in range(cols):
                    matrix[r][c] = 0
        for c in range(1, cols):
            if matrix[0][c] == 0:
                print 'clear col %s' % c
                for r in range(rows):
                    matrix[r][c] = 0

        if clear_c0:
            for r in range(rows):
                matrix[r][0] = 0
        if clear_r0:
            for c in range(cols):
                matrix[0][c] = 0

s = Solution()
s.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])

