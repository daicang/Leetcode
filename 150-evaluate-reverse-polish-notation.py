from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            # print(stack)
            if token.isnumeric() or token[1:].isnumeric():
                stack.append(int(token))
            else:
                n1 = stack.pop()
                n2 = stack.pop()

                if token == '+':
                    # print('add', n1, n2)
                    stack.append(n1+n2)
                elif token == '-':
                    stack.append(n2-n1)
                elif token == '*':
                    stack.append(n1*n2)
                else:
                    # print('div', n1, n2)
                    stack.append(int(n2/n1))
        # print(stack)
        return stack[0]

data = [
    ["4","13","5","/","+"],
    ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
]
s = Solution()
for d in data:
    print(s.evalRPN(d))
