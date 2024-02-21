




class Token:
    def __init__(self, typ=None, val=None):
        self.typ = typ
        self.val = val

    def __repr__(self):
        if self.val is not None:
            return str(self.val)
        return str(self.typ)


class Solution:
    def lexer(self, s):
        tokens = []
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
        op = None
        for token in tokens:
            if isinstance(token, int):
                stack.append(sign * token)
                sign = 1
                # LR(2) parsing
                if op == '*':
                    stack.append(stack.pop() * stack.pop())
                    op = None
                elif op == '/':
                    n1 = stack.pop()
                    n2 = stack.pop()
                    if n1*n2 < 0:
                        stack.append(-(-n2//n1))
                    else:
                        stack.append(n2//n1)
                    op = None
            elif token == '+':
                sign = 1
            elif token == '-':
                sign = -1
            else:
                assert token in ('*', '/')
                assert op is None
                op = token
        return sum(stack)

    def calculate(self, s: str) -> int:
        tokens = self.lexer(s)
        return self.eval(tokens)


    def calculate_0(self, s: str) -> int:
        # Lexing
        i = 0
        tokens = []

        while i < len(s):
            while i < len(s) and s[i] == ' ':
                i += 1
            if i == len(s):
                break

            if s[i].isdigit():
                val = 0
                while i < len(s) and s[i].isdigit():
                    val *= 10
                    val += ord(s[i]) - ord('0')
                    i += 1
                tokens.append(Token('number', val))

            else:
                tokens.append(Token(s[i], None))
                i += 1

        # First iteration, solve mul and div
        tmp = []
        i = 0
        # print(tokens)

        while i < len(tokens):
            token = tokens[i]
            match token.typ:
                case '*':
                    lval = tmp.pop().val
                    i += 1
                    rval = tokens[i].val
                    tmp.append(Token('number', lval * rval))
                case '/':
                    lval = tmp.pop().val
                    i += 1
                    rval = tokens[i].val
                    tmp.append(Token('number', lval // rval))
                case _:
                    tmp.append(token)
            i += 1
        # print(tmp)
        # Second iteration, solve add and sub
        i = 0
        tokens = tmp
        result = 0

        while i < len(tokens):
            token = tokens[i]
            match token.typ:
                case '+':
                    i += 1
                    rval = tokens[i].val
                    result += rval
                case '-':
                    i += 1
                    rval = tokens[i].val
                    result -= rval
                case _:
                    result = token.val
            i += 1

        return result

s = Solution()

inputs = [
    "3+2*2",  # 7
    " 3/2 ",  # 1
    " 3+5 / 2 ",  # 5
    "14-3/2",  # 13
]

for i in inputs:
    print(s.calculate(i))
