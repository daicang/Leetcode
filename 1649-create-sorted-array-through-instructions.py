
class BitIndexTree:
    def __init__(self, n):
        self.arr = [0] * (n+1)
        self.n = n

    def update(self, i, val):
        while i <= self.n:
            self.arr[i] += val
            i += i & (-i)

    def get_sum(self, i):
        s = 0
        while i > 0:
            s += self.arr[i]
            i -= i & (-i)
        return s


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        mod = 10**9 + 7
        limit = 10**5 + 10

        t1 = BitIndexTree(limit)
        t2 = BitIndexTree(limit)

        s = 0
        for i in instructions:
            t1.update(i, 1)
            t2.update(limit-i, 1)
            s += min(t1.get_sum(i-1), t2.get_sum(limit-i-1))
            s %= mod

        return s
