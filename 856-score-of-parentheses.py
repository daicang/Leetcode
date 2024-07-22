class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:
                val = 0
                if stack[-1] == '(':
                    val = 1
                else:
                    while stack[-1] != '(':
                        val += stack.pop()
                    val *= 2
                stack.pop()
                stack.append(val)
        return sum(stack)
