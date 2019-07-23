class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool

        Recursion with memorization
        """

        p_formatted = []
        adjacent = False
        for ch in p:
            if ch == '*':
                if adjacent:
                    continue
                adjacent = True
            else:
                adjacent = False
            p_formatted.append(ch)
        p = ''.join(p_formatted)

        ls, lp = len(s), len(p)

        memo = {}

        def matcher(si, pi):
            key = (si, pi)
            if key in memo:
                return memo[key]

            while True:
                if pi == lp:
                    return si == ls

                if si == ls:
                    for i in range(pi, lp):
                        if p[i] != '*':
                            memo[key] = False
                            return False
                    memo[key] = True
                    return True

                if p[pi] == '*':
                    for i in range(si, ls+1):
                        if matcher(i, pi+1):
                            memo[key] = True
                            return True
                    memo[key] = False
                    return False

                else:
                    if p[pi] != '?' and s[si] != p[pi]:
                        memo[key] = False
                        return False

                    # match
                    si += 1
                    pi += 1

        return matcher(0, 0)

    def isMatch_dp(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        p_formatted = []
        adjacent = False
        for ch in p:
            if ch == '*':
                if adjacent:
                    continue
                adjacent = True
            else:
                adjacent = False
            p_formatted.append(ch)
        p = ''.join(p_formatted)

        ls, lp = len(s), len(p)

        # dp[pi][si]: p[0..pi] matches s[0..si]
        dp = []
        for _ in range(lp+1):
            dp.append([False] * (ls+1))
        dp[0][0] = True

        for pi in range(1, lp+1):
            if p[pi-1] == '*':
                flag = False
                for si in range(ls+1):
                    if dp[pi-1][si]:
                        flag = True

                    dp[pi][si] = flag

            elif p[pi-1] == '?':
                for si in range(1, ls+1):
                    dp[pi][si] = dp[pi-1][si-1]

            else:
                for si in range(1, ls+1):
                    dp[pi][si] = (p[pi-1] == s[si-1]) and (dp[pi-1][si-1])

        return dp[lp][ls]


inputs = [
    ['aa', '*'],
    ["aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******b"],
    ["adceb", "*a*b"],
    ["babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb", "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"],
]

s = Solution()
for input in inputs:
    print s.isMatch(*input), s.isMatch_dp(*input)

