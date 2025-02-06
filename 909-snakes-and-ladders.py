class Solution:
    def snakesAndLadders_1(self, board):
        n = len(board)
        need = {1: 0}
        bfs = [(1, [1])]
        for x, path in bfs:
            for i in range(x + 1, x + 7):
                a, b = divmod((i - 1), n)
                nxt = board[~a][b if a % 2 == 0 else ~b]
                if nxt > 0: i = nxt
                if i == n * n:
                    print(path+[i])
                    return need[x] + 1
                if i not in need:
                    need[i] = need[x] + 1
                    bfs.append((i, path[:]+[i]))
        return -1

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        rows = len(board)

        def getval(i):
            q, r = divmod(i-1, rows)
            row = rows-1-q
            col = r if q % 2 == 0 else ~r
            val = board[row][col]
            return val if val > 0 else i

        visited = [False] * (rows**2+1)
        q = [(1, [1])]
        steps = 0

        while q:
            nq = []
            while q:
                i, path = q.pop()
                if visited[i]:
                    continue

                visited[i] = True

                if i == rows**2:
                    return steps

                for j in range(i+1, i+7):
                    if j <= rows**2:
                        jval = getval(j)
                        nq.append((jval, path[:]+[jval]))

            q = nq
            steps += 1
        return -1
