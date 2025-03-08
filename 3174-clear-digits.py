class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch.isdigit():
                if stack and not stack[-1].isdigit():
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
        return ''.join(stack)
