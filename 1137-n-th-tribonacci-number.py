class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        a0 = 0
        a1 = 1
        a2 = 1
        for _ in range(n-2):
            a0, a1, a2 = a1, a2, a0+a1+a2

        return a2
