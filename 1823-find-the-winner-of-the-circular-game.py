
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        result = 0
        for i in range(1, n+1):
            result += k
            result %= i
        return result + 1


inputs = [
    (5, 2),
    (6, 5)
]

s = Solution()

for i in inputs:
    print(s.findTheWinner(*i))
