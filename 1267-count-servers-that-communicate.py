class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        rows = [0] * len(grid)
        cols = [0] * len(grid[1])

        for row_id, row in enumerate(grid):
            for col_id, val in enumerate(row):
                if val == 1:
                    rows[row_id] += 1
                    cols[col_id] += 1

        count = 0

        for row_id, row in enumerate(grid):
            for col_id, val in enumerate(row):
                if val == 1:
                    if rows[row_id] > 1 or cols[col_id] > 1:
                        count += 1

        return count

s = Solution()

inputs = [
    [[1,0],[0,1]],
    [[1,0],[1,1]],
    [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
]

for i in inputs:
    print s.countServers(i)
