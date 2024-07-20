class Solution:
    def minimumLength(self, s: str) -> int:
        c = Counter(s)
        l = 0
        for v in c.values():
            while v >= 3:
                v, r = divmod(v, 3)
                v += r
            l += v
        return l
