# 10-regular-expression-matching.py

class Solution(object):
    def isMatch_tle(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Correct, but TLE
        # Same method ACed in C/C++, I've tried eliminate function call,
        # which saved around 1.5s
        ls, lp = len(s), len(p)
        
        def iter(si, pi):
            while si < ls and pi < lp:
                if pi == lp - 1 or p[pi+1] != '*':
                    if p[pi] == '*' or s[si] == p[pi]:
                        si, pi = si+1, pi+1
                    else:
                        return False
                else:
                    if p[pi] == '*' or s[si] == p[pi]:
                        return iter(si, pi+2) or iter(si+1, pi)
                    else:
                        pi += 2

            while pi+1 < lp and p[pi+1] == '*': pi += 2
            
            return si == ls and pi >= lp
                    
        return iter(0, 0)

    def isMatch(self, s, p):
        # table[p][s]
        # table[0][0]: two empty string
        # table[1][1]: is p[0] matching s[0]
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        table[0][0] = True
        ls, lp = len(s), len(p)
        
        for i in range(2, lp+1):
            if p[i-1] == '*': table[i][0] = table[i-2][0]

        for pi in range(1, lp+1):
            for si in range(1, ls+1):
                if p[pi-1] != '*':
                    table[pi][si] = table[pi-1][si-1] and \
                                    (p[pi-1] == s[si-1] or p[pi-1] == '.')
                else:
                    table[pi][si] = table[pi-1][si] or table[pi-2][si]
                    if p[pi-2] == s[si-1] or p[pi-2] == '.':
                        table[pi][si] |= table[pi][si-1]

        return table[-1][-1]
            
        
        

s = Solution()

print(s.isMatch("abc", "abc"))
print(s.isMatch("abc", "ab*bc"))
print(s.isMatch("abbc", "ab*bc"))
print(s.isMatch("aaaaaaaaaaaaac", "a*a*a*a*a*a*a*a*a*a*a*b"))
