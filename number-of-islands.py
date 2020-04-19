from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visited = []
        for _ in range(rows):
            visited.append([False] * cols)

        def visit(row, col):
            targets = [(row, col)]
            while targets:
                row, col = targets.pop()
                if visited[row][col]:
                    continue
                visited[row][col] = True
                if row > 0 and grid[row-1][col] == '1':
                    targets.append((row-1, col))
                if row < rows-1 and grid[row+1][col] == '1':
                    targets.append((row+1, col))
                if col > 0 and grid[row][col-1] == '1':
                    targets.append((row, col-1))
                if col < cols-1 and grid[row][col+1] == '1':
                    targets.append((row, col+1))


        for row in range(rows):
            for col in range(cols):
                if visited[row][col] or grid[row][col] == '0':
                    continue

                visit(row, col)
                islands += 1

        return islands