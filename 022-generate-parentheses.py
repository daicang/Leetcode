class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n < 1:
            return []

        stack = [('(', 1, n-1)]
        ret = []

        while stack:
            s, incomplete, remains = stack.pop()
            if incomplete == 0 and remains == 0:
                ret.append(s)
                continue

            if incomplete > 0:
                stack.append(s+')', incomplete-1, remains)
            if remains > 0:
                stack.append(s+'(', incomplete+1, remains-1)

        return ret

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n < 1:
            return ['']

        ret = []
        for c in range(n):
            for l in self.generateParenthesis(c):
                for r in self.generateParenthesis(n-c-1):
                    ret.append('(%s)%s' % (l, r))
        return ret
