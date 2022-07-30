




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
    "3+2*2",
    " 3/2 ",
    " 3+5 / 2 ",
]

for i in inputs:
    print(s.calculate(i))
