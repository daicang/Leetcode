# 10-regular-expression-matching.py

from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @cache
        def solve(si, pi):
            if pi == len(p):
                # pattern has been used up
                # must match entire s
                return si == len(s)

            if si < len(s) and (s[si] == p[pi] or p[pi] == '.'):
                if pi < len(p)-1 and p[pi+1] == '*':
                    # s=ab match p=a*b
                    # next state:
                    # (wildcard match a): s=b, p=a*b
                    # (wildcard skip): s=ab, p=b
                    return solve(si+1, pi) or solve(si, pi+2)
                else:
                    # match next character
                    return solve(si+1, pi+1)
            else:
                # unmatch
                # 1) skip a* 2) unmatch
                if pi < len(p)-1 and p[pi+1] == '*':
                    return solve(si, pi+2)
                else:
                    return False

        return solve(0, 0)


s = Solution()

data = [
    ['abc', 'abc'], #t
    ("abc", "ab*bc"), #t
    ("abbc", "ab*bc"), #t
    ("aaaaaaaaaaaaac", "a*a*a*a*a*a*a*a*a*a*a*b"), #f
]

for d in data:
    print(s.isMatch(*d))
