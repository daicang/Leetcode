class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        class Level(object):
            def __init__(self, reverse=True):
                self.elems = []
                self.reverse = reverse

            def __str__(self):
                s = ''.join([str(e) for e in self.elems])
                if self.reverse:
                    return s[::-1]
                return s

        s += ')'
        lv0 = Level(False)
        val = ''
        stack = [lv0]

        for ch in s:
            if ch == '(':
                stack[-1].elems.append(val)
                stack.append(Level())
                val = ''

            elif ch == ')':
                stack[-1].elems.append(val)
                lv = stack.pop()
                if stack:
                    stack[-1].elems.append(lv)
                val = ''

            else:
                val += ch

        return str(lv0)


s = Solution()

inputs = [
    ["(abcd)", "dcba"],
    ["(ed(et(oc))el)", 'leetcode'],
    ["a(bcdefghijkl(mno)p)q","apmnolkjihgfedcbq"],
    ["(u(love)i)", "iloveu"],
    ["ta()usw((((a))))", "tauswa"]
]

for i in inputs:
    result = s.reverseParentheses(i[0])
    if result != i[1]:
        print i[0], result, i[1]


