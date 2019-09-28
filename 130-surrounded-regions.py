class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        rows = len(board)
        cols = len(board[0])

        marker = []
        for _ in range(rows):
            marker.append([False] * cols)

        visited = []
        for _ in range(rows):
            visited.append([False] * cols)

        def bfs(r, c):
            if visited[r][c]:
                return

            def avail(r, c):
                return 0<=c<cols and 0<=r<rows and not visited[r][c] and board[r][c] == 'O'

            queue = [(r,c)]
            while queue:
                r, c = queue.pop()
                marker[r][c] = True
                for next_r, next_c in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                    if avail(next_r, next_c):
                        visited[next_r][next_c] = True
                        queue.append((next_r, next_c))

        for row in (0, rows-1):
            for col in range(cols):
                if board[row][col] == 'O':
                    bfs(row, col)

        for col in (0, cols-1):
            for row in range(rows):
                if board[row][col] == 'O':
                    bfs(row, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O' and not marker[row][col]:
                    board[row][col] = 'X'


s = Solution()

inputs = [
    [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]],
]

for i in inputs:
    s.solve(i)
    print i

