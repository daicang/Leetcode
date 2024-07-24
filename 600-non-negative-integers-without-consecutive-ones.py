class Solution:
    def findIntegers(self, n: int) -> int:
        @cache
        def solve(i):
            # allow 0 to be the first bit
            if i == 0:
                return 1
            if i == 1:
                return 2
            # 0, solve(i-1)
            # 1, 0, solve(i-2)
            return solve(i-1) + solve(i-2)

        s = 0
        prev_bit = False
        for i in range(30, -1, -1):
            if n & (1<<i):
                s += solve(i)
                if prev_bit:
                    s -= 1
                    break
                prev_bit = True
            else:
                prev_bit = False

        return s + 1
