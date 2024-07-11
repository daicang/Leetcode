
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        # time: O(row*col)
        # space: O(row*col)
        max_kill = 0
        rows, cols = len(grid), len(grid[0])

        kills = []
        for _ in range(rows):
            kills.append([None] * cols)

        def calc_kill_row(row, col):
            if col > 0 and kills[row][col-1][0] > 0:
                return kills[row][col-1][0]
            count = 0
            for c in range(col-1, -1, -1):
                if grid[row][c] == 'E':
                    count += 1
                elif grid[row][c] == 'W':
                    break
            for c in range(col+1, cols):
                ch = grid[row][c]
                if ch == 'E':
                    count += 1
                elif ch == 'W':
                    break
            return count

        def calc_kill_col(row, col):
            if row > 0 and kills[row-1][col][1] > 0:
                return kills[row-1][col][1]
            count = 0
            # -1 is to end, not 0!
            for r in range(row-1, -1, -1):
                ch = grid[r][col]
                if ch == 'E':
                    count += 1
                elif ch == 'W':
                    break
            for r in range(row+1, rows):
                ch = grid[r][col]
                if ch == 'E':
                    count += 1
                elif ch == 'W':
                    break
            return count

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != '0':
                    kills[row][col] = (0, 0)
                else:
                    kill_row = calc_kill_row(row, col)
                    kill_col = calc_kill_col(row, col)
                    kills[row][col] = (kill_row, kill_col)
                    max_kill = max(max_kill, kill_row+kill_col)

        return max_kill
