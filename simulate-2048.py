
import random

# Simulate 2048 game
class Game:

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
                i += 1
                j -= 1

    def transpose(self):
        for i in range(self.n):
            for j in range(i+1, self.n):
                self.board[i][j], self.board[j][i] = self.board[j][i], self.board[i][j]

    def move(self, direction):
        if self.finished:
            return

        if direction == 'r':
            self.move_right()
        elif direction == 'l':
            self.move_left()
        elif direction == 'u':
            self.move_up()
        elif direction == 'd':
            self.move_down()
        else:
            raise Exception(f'invalid direction: {direction}')

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

    def print(self):
        print('')
        for row in self.board:
            print(' '.join([str(i) for i in row]))
        print('')

    def new2(self):
        while True:
            x = random.randint(0, self.n-1)
            y = random.randint(0, self.n-1)
            if self.board[x][y] != 0:
                continue
            self.board[x][y] = 2
            return

    def run(self):
        if self.finished:
            print('Finished!')
            return

        while True:
            self.new2()
            self.print()
            cmd = input('input: [u]p, [d]own, [l]eft, [r]ight')
            self.move(cmd)
            self.print()
            if self.finished:
                print('Finished!')
                break


g = Game(4)
g.run()
