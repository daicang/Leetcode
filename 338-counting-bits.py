class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        for x in range(1, n+1):
            ans[x] = ans[x & (x-1)] + 1
            # or
            # ans[x] = ans[x >> 1] + (x & 1)
        return ans
