class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        board = []
        for _ in range(3):
            board.append([None] * 3)

        for i, move in enumerate(moves):
            if i % 2 == 0:
                player = 'A'
            else:
                player = 'B'
            x, y = move
            board[x][y] = player

        def check(vec):
            player = None
            for val in vec:
                if val is None:
                    return None

                if player is None:
                    player = val
                else:
                    if player != val:
                        return None
            return player

        vecs = []
        for row in range(3):
            vecs.append(board[row])

        for col in range(3):
            vecs.append([board[r][col] for r in range(3)])

        vecs.append([board[0][0], board[1][1], board[2][2]])
        vecs.append([board[0][2], board[1][1], board[2][0]])

        for vec in vecs:
            val = check(vec)
            if val:
                return val

        for row in board:
            if None in row:
                return 'Pending'
        return 'Draw'


s = Solution()

data = [
    [[0,0],[2,0],[1,1],[2,1],[2,2]],
    [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]],
    [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]],
    [[0,0],[1,1]]
]

for d in data:
    print s.tictactoe(d)
