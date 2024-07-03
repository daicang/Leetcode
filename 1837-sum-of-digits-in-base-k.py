class Solution:
    def sumBase(self, n: int, k: int) -> int:
        s = 0
        while n:
            n, r = divmod(n, k)
            s += r
        return s
