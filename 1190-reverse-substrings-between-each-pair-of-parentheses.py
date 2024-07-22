class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != ')':
                stack.append(ch)
            else:
                arr = []
                while stack:
                    ch1 = stack.pop()
                    if ch1 == '(':
                        break
                    arr.append(ch1)
                stack.extend(arr)
        return ''.join(stack)
