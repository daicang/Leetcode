class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        stack = []
        for ch in S:
            if ch == 'a':
                stack.append('b')
            else:
                if len(stack) == 0:
                    return False
                want = stack.pop()
                if ch != want:
                    return False
                if ch == 'b':
                    stack.append('c')

        if len(stack) == 0:
            return True
        return False


s = Solution()
inputs = [
    "aabcbc",
    "abcabcababcc",
    "abccba",
    "cababc",
]
for input in inputs:
    print(s.isValid(input))
