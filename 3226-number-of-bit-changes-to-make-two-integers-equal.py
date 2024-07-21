class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n | k != n:
            return -1
        i = (n | k) ^ k
        count = 0
        while i:
            i, c = divmod(i, 2)
            count += c
        return count