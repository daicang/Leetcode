
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parens = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        for ch in s:
            if ch in parens:
                stack.append(parens[ch])
            else:
                if not stack or stack.pop() != ch:
                    return False

        return True
