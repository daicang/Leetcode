class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        expects = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for ch in s:
            if ch in expects:
                stack.append(expects[ch])
            else:
                if len(stack) == 0:
                    return False
                expected = stack.pop()
                if ch != expected:
                    return False
        return len(stack) == 0



s = Solution()
print(s.isValid("([)]"))
