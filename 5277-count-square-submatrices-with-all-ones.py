class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        def check_matrix(row, col, size):
            for r in range(row, row+size):
                for c in range(col, col+size):
                    if matrix[r][c] == 0:
                        return False
                    # print '%s,%s size=%s' % (row, col, size)

            return True

        total_count = 0

        for size in range(1, min(rows, cols)+1):
            count = 0
            for row in range(rows-size+1):
                for col in range(cols-size+1):
                    if check_matrix(row, col, size):
                        count += 1

            if count == 0:
                break

            # print 'size=%s, count=%s\n' % (size, count)
            total_count += count

        return total_count

s = Solution()

data = [
    [
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]
    ],
    [
        [1,0,1],
        [1,1,0],
        [1,1,0]
    ]
]

for d in data:
    print s.countSquares(d)

