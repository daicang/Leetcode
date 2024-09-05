class Solution:
    def strangePrinter(self, s: str) -> int:

        @cache
        def solve(begin, end):
            if begin > end:
                return 0

            rounds = 1 + solve(begin+1, end)
            for i in range(begin+1, end+1):
                if s[begin] == s[i]:
                    rounds = min(rounds, solve(begin, i-1)+solve(i+1, end))
            return rounds

        return solve(0, len(s)-1)
