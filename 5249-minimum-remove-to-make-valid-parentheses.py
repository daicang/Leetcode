class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        remove = []
        for i, val in enumerate(s):
            if val == '(':
                stack.append(i)
            elif val == ')':
                if stack:
                    stack.pop()
                else:
                    remove.append(i)

        remove.extend(stack)

        new = []
        for i, val in enumerate(s):
            if i not in remove:
               new.append(val)

        return ''.join(new)

s = Solution()

inputs = [
    "lee(t(c)o)de)",
    "a)b(c)d",
    "))((",
    "(a(b(c)d)"
]

for i in inputs:
    print s.minRemoveToMakeValid(i)

