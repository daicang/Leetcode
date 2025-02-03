class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows, cols = len(board), len(board[0])
        # 0->0: 0
        # 0->1: -1
        # 1->1: 1
        # 1->0: 2

        def count(r, c):
            count = 0
            for nr in range(max(0, r-1), min(rows, r+2)):
                for nc in range(max(0, c-1), min(cols, c+2)):
                    if nr == r and nc == c:
                        continue
                    if board[nr][nc] > 0:
                        count += 1
            return count

        def update(r, c, count):
            if board[r][c] == 0:
                if count == 3:
                    board[r][c] = -1
            else:
                if count < 2 or count > 3:
                    board[r][c] = 2


        for r in range(rows):
            for c in range(cols):
                update(r, c, count(r, c))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == -1:
                    board[r][c] = 1
                elif board[r][c] == 2:
                    board[r][c] = 0
