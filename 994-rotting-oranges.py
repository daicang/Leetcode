class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        tm = 0

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))

        while q:
            x, y, step = q.popleft()
            tm = step
            for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    q.append((nx, ny, step+1))
                    grid[nx][ny] = 2

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return tm
