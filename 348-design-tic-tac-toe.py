
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = []
        for _ in range(n):
            row = [0] * n
            self.board.append(row)

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        for i in range(self.n):
            if self.board[row][i] != player:
                win_row = False
                break
        else:
            return player

        for i in range(self.n):
            if self.board[i][col] != player:
                win_col = False
                break
        else:
            return player

        if row == col:
            for i in range(self.n):
                if self.board[i][i] != player:
                    win_dia = False
                    break
            else:
                return player

        if row + col == self.n - 1:
            for i in range(self.n):
                j = self.n-1-i
                if self.board[i][j] != player:
                    win_dia = False
                    break
            else:
                return player

        return 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)