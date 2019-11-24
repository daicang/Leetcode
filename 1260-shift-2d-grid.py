class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        if not grid or not grid[0]:
            return grid

        rows = len(grid)
        cols = len(grid[0])

        for _ in range(k):
            last_col = []

            for col in range(cols-1, -1, -1):
                if col == cols-1:
                    for row in range(rows):
                        last_col.append(grid[row][col])

                if col == 0:
                    for row, val in enumerate(last_col):
                        grid[(row+1)%rows][0] = val
                else:
                    for row in range(rows):
                        grid[row][col] = grid[row][col-1]

        return grid


inputs = [
    [[[1,2,3],[4,5,6],[7,8,9]], 1],
    [[[1],[2],[3],[4],[7],[6],[5]], 23],
]

s = Solution()

for i in inputs:
    print s.shiftGrid(*i)
