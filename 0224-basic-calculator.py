

from types import SimpleNamespace

from collections import deque


class Token:
    def __init__(self, typ=None, val=None):
        self.type = typ
        self.val = val

    def __repr__(self):
        if self.val is not None:
            return str(self.val)
        return str(self.type)

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
                val = 0
                while i < len(s) and s[i].isdigit():
                    val *= 10
                    val += int(s[i])
                    i += 1
                tokens.append(val)
            elif s[i] == '+':
                i += 1
                tokens.append('add')
            elif s[i] == '-':
                i += 1
                tokens.append('sub')
            elif s[i] == '(':
                i += 1
                tokens.append('lpr')
            elif s[i] == ')':
                i += 1
                tokens.append('rpr')
            else:
                raise Exception(f'invalid token {s[i]}')

        return tokens

    def eval_stack(self, tokens):
        # eval braces with stack
        stack = []
        sign = 1
        for token in tokens:
            if isinstance(token, int):
                stack.append(sign * token)
                sign = 1
            elif token == 'add':
                sign = 1
            elif token == 'sub':
                sign = -1
            elif token == 'lpr':
                stack.append(sign)
                stack.append(token)
                sign = 1
            elif token == 'rpr':
                value = 0
                while True:
                    token = stack.pop()
                    if isinstance(token, int):
                        value += token
                    else:  # lpr
                        break
                sign = stack.pop()
                stack.append(sign * value)
            else:
                raise Exception('invalid token')
        return sum(stack)

    def eval(self, tokens):
        # eval braces with recursion
        result = 0
        sign = 1
        while tokens:
            token = tokens.popleft()
            if isinstance(token, int):
                result += sign * token
                sign = 1
            elif token == 'add':
                continue
            elif token == 'sub':
                sign = -1
            elif token == 'lpr':
                result += sign * self.eval(tokens)
                sign = 1
            elif token == 'rpr':
                break
            else:
                raise Exception('unknown token')

        return result


    def calculate(self, s: str) -> int:
        tokens = self.lexer(s)
        # return self.eval(tokens)
        return self.eval_stack(tokens)



    def calculate_0(self, s: str) -> int:
        # Lexing
        tk = SimpleNamespace()
        tk.num = 'num'
        tk.add = '+'
        tk.sub = '-'
        tk.lparen = '('
        tk.rparen = ')'

        i = 0
        tokens = []

        while i < len(s):
            while i < len(s) and s[i] == ' ':
                i += 1
            if i == len(s):
                break

            typ = None
            val = 0

            if s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    val *= 10
                    val += ord(s[i]) - ord('0')
                    i += 1
                tokens.append(Token(tk.num, val))

            else:
                match s[i]:
                    case '+':
                        typ = tk.add
                    case '-':
                        typ = tk.sub
                    case '(':
                        typ = tk.lparen
                    case ')':
                        typ = tk.rparen
                    case _:
                        assert False, "invalid token %s" % s[i]

                tokens.append(Token(typ, None))
                i += 1

        # print(tokens)
        stack = []

        # Solve all parens, in reverse order
        for token in tokens[::-1]:
            match token.typ:
                case tk.lparen:
                    paren_sum = 0
                    positive = True
                    while stack[-1].typ != tk.rparen:
                        token = stack.pop()
                        match token.typ:
                            case tk.num:
                                if positive:
                                    paren_sum += token.val
                                else:
                                    paren_sum -= token.val
                                positive = True
                            case tk.sub:
                                positive = not positive
                            case _:
                                pass
                    stack.pop() # pop right paren
                    stack.append(Token(tk.num, paren_sum))
                case _:
                    stack.append(token)

        stack_sum = 0
        positive = True

        # Solve thre rest with no parenthese, in reverse order
        while stack:
            token = stack.pop()
            match token.typ:
                case tk.add:
                    pass
                case tk.sub:
                    positive = not positive
                case tk.num:
                    if positive:
                        stack_sum += token.val
                    else:
                        stack_sum -= token.val
                    positive = True # Reset
                case _:
                    assert False, stack

        return stack_sum



s = Solution()

inputs = [
    ['1 + 1', 2],
    ['2-1 + 2', 3],
    ["(1+(4+5+2)-3)+(6+8)", 23],
    [" 2-1 + 2 ", 3],
    ['1', 1],
    ['(1)', 1],
    ['-2+ 1', -1],
    ['(-1)', -1],
    ['-(1)', -1],
]

for i in inputs:
    arg, val = i
    result = s.calculate(arg)
    assert result == val, (arg, result, val)
    # print(s.calculate(i))
