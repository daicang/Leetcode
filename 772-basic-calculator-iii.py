
from collections import deque

class Solution:
    def lexer(self, s):
        tokens = deque()
        i = 0

        while True:
            while i < len(s) and s[i] == ' ':
                i += 1
            if i == len(s):
                break
            if s[i].isdigit():
                value = 0
                while i < len(s) and s[i].isdigit():
                    value = value * 10 + int(s[i])
                    i += 1
                tokens.append(value)
            else:
                tokens.append(s[i])
                i += 1
        return tokens

    def eval(self, tokens):
        stack = []
        sign = 1

        while tokens:
            token = tokens.popleft()
            if isinstance(token, int):
                n = token * sign
                sign = 1
                if stack and stack[-1] == '*':
                    # LR(2)
                    stack.pop()
                    m = stack.pop()
                    stack.append(n * m)
                elif stack and stack[-1] == '/':
                    stack.pop()
                    m = stack.pop()
                    if n*m < 0:
                        stack.append(-(-m//n))
                    else:
                        stack.append(m//n)
                else:
                    stack.append(n)
            elif token == '+':
                sign = 1
            elif token == '-':
                sign = -1
            elif token in '*/':
                stack.append(token)
            elif token == '(':
                value = self.eval(tokens)
                tokens.appendleft(value)
            elif token == ')':
                break
            else:
                raise Exception('invalid token')

        return sum(stack)

    def calculate(self, s: str) -> int:
        tokens = self.lexer(s)
        return self.eval(tokens)


s = Solution()

data = [
    '1+1',  # 2
    "6-4/2",  # 4
    "2*(5+5*2)/3+(6/2+8)",  # 21
]

for d in data:
    print(s.calculate(d))
