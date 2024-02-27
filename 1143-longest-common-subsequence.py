

class Solution:
    def longestCommonSubsequence_dp0(self, text1: str, text2: str) -> int:
        # dp, AC but slow
        n1 = len(text1)
        n2 = len(text2)

        cache = {}

        def solve(i1, i2):
            if i1 < 0 or i2 < 0:
                return 0
            key = f'{i1}-{i2}'
            if key not in cache:
                if text1[i1] == text2[i2]:
                    ret = 1 + solve(i1-1, i2-1)
                else:
                    ret = max(solve(i1, i2-1), solve(i1-1, i2))
                cache[key] = ret
            return cache[key]

        return solve(n1-1, n2-1)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)

        cache_prev = [0] * l2
        cache_curr = [0] * l2

        for i1 in range(l1):
            for i2 in range(l2):
                if text1[i1] == text2[i2]:
                    if i2 == 0:
                        cache_curr[i2] = 1
                    else:
                        cache_curr[i2] = cache_prev[i2-1] + 1
                else:
                    if i2 == 0:
                        cache_curr[0] = cache_prev[0]
                    else:
                        cache_curr[i2] = max(cache_prev[i2], cache_curr[i2-1])

            cache_prev = cache_curr
            cache_curr = [0] * l2

        return cache_prev[-1]


s = Solution()

data = [
    ["abcde", "ace"],  # 3
    ['abc', 'abc'],  # 3
    ['abc', 'def'],  # 0
    ['oxcpqrsvwf', 'shmtulqrypy'],  # 2
]

for d in data:
    print(s.longestCommonSubsequence_dp0(*d), s.longestCommonSubsequence(*d))
