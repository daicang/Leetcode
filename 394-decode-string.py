
class Token:

    lparen = '['
    rparen = ']'
    num = 'num'
    string = 'string'

    def __init__(self, val):
        self.type = 'unknown'
        self.val = val

        if val == '[':
            self.type = self.lparen
        elif val == ']':
            self.type = self.rparen
        elif isinstance(val, int):
            self.type = self.num
        else:
            self.type = self.string


class Solution:

    def lexer(self, s):
        tokens = []
        i = 0

        while i < len(s):
            if s[i].isdigit():
                n = 0
                while i < len(s) and s[i].isdigit():
                    n *= 10
                    n += int(s[i])
                    i += 1
                tokens.append(Token(n))
            elif s[i] == '[':
                tokens.append(Token('['))
                i += 1
            elif s[i] == ']':
                tokens.append(Token(']'))
                i += 1
            else:
                chs = []
                while i < len(s) and 'a' <= s[i] <= 'z':
                    chs.append(s[i])
                    i += 1
                tokens.append(Token(''.join(chs)))

        return tokens

    def parse_string(self, tokens) -> str:
        # str := <num>[<str>] | <str><str>
        # recursive solution
        if not tokens:
            return ''

        token = tokens.pop(0)
        if token.type == Token.num:
            # <num>[<str>]
            n = token.val
            assert tokens.pop(0).type == Token.lparen

            counter = 0
            content = []

            while tokens:
                token = tokens.pop(0)

                if token.type == Token.lparen:
                    counter += 1

                elif token.type == Token.rparen:
                    if counter == 0:
                        break
                    counter -= 1

                content.append(token)

            return n * self.parse_string(content) + self.parse_string(tokens)

        else:
            # <str><str>
            assert token.type == Token.string, token.type
            return token.val + self.parse_string(tokens)


    def decodeString(self, s: str) -> str:
        tokens = self.lexer(s)
        return self.parse_string(tokens)


s = Solution()
data = [
    '3[a2[c]]',
    '2[a]3[c]4[b]5[d]'
]

for d in data:
    print(s.decodeString(d))
