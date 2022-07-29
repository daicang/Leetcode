

from types import SimpleNamespace


class Token:
    def __init__(self, typ=None, val=None):
        self.typ = typ
        self.val = val

    def __repr__(self):
        if self.val is not None:
            return str(self.val)
        return str(self.typ)

class Solution:
    def calculate(self, s: str) -> int:
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
