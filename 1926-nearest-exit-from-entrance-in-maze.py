class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque([(entrance[0], entrance[1], 0)])
        rows, cols = len(maze), len(maze[0])
        ent = True

        while q:
            x, y, step = q.popleft()
            if (ent is False) and (x == 0 or y == 0 or x == rows-1 or y == cols-1):
                return step
            for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == '.':
                    maze[nx][ny] = '+'
                    q.append((nx, ny, step+1))
            maze[x][y] = '+'
            ent = False

        return -1
