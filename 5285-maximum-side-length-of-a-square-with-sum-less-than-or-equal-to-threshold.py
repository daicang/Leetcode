class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        rows = len(mat)
        cols = len(mat[0])

        sum_square = []
        for _ in range(rows+1):
            sum_square.append([0] * (cols+1))

        for r in range(1, rows+1):
            for c in range(1, cols+1):
                sum_square[r][c] = sum_square[r-1][c] + sum_square[r][c-1] + mat[r-1][c-1] - sum_square[r-1][c-1]

        def get_sum(x, y, size):
            return sum_square[x+size][y+size] - sum_square[x+size][y] - sum_square[x][y+size] + sum_square[x][y]

        for size in range(1, min(rows, cols)+1):
            minimum = None
            for x in range(rows+1-size):
                for y in range(cols+1-size):
                    s_sum = get_sum(x, y, size)

                    if minimum is None or s_sum < minimum:
                        minimum = s_sum

            if minimum > threshold:
                return size - 1

        return size


data = [
    [[[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4],
    [[[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], 1],
    [[[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], 6],
    [[[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], 40184]
]

s = Solution()
for d in data:
    print s.maxSideLength(*d)
