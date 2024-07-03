
# Simulate 2048 game
class Game:

    move_up = 'u'
    move_down = 'd'
    move_left = 'l'
    move_right = 'r'

    def __init__(self, n):
        self.finished = False
        self.n = n
        self.board = []
        for _ in range(n):
            self.board.append([0] * n)

    def put(self, x, y):
        assert 0 <= x < self.n
        assert 0 <= y < self.n
        assert self.board[x][y] == 0
        self.board[x][y] = 2

    def reverse_rows(self):
        for i in range(self.n):
            row = self.board[i]
            i, j = 0, self.n-1
            while i < j:
                row[i], row[j] = row[j], row[i]

    def transpose(self):
        for i in range(self.n):
            for j in range(i+1, self.n):
                self.board[i][j], self.board[j][i] = self.board[j][i], self.board[i][j]

    def move(self, d):
        if self.finished:
            return
        if d == self.move_right:
            self.move_right()
        elif d == self.move_left:
            self.move_left()
        elif d == self.move_up:
            self.move_up()
        elif d == self.move_down:
            self.move_down()
        else:
            raise Exception('invalid direction')

    def move_up(self):
        self.transpose()
        self.move_left()
        self.transpose()

    def move_down(self):
        self.transpose()
        self.move_right()
        self.transpose()

    def move_left(self):
        for i in range(self.n):
            row = self.board[i]
            stack = []
            for val in row:
                if val == 0:
                    continue
                if stack and stack[-1] == val:
                    stack.pop()
                    newval = val*2
                    if newval == 2048:
                        self.finished = True
                    stack.append(newval)
                else:
                    stack.append(val)
            for j in range(self.n):
                if j < len(stack):
                    row[j] = stack[j]
                else:
                    row[j] = 0

    def move_right(self):
        self.reverse_rows()
        self.move_left()
        self.reverse_rows()
