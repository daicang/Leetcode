class Solution:
    def isHappy(self, n: int) -> bool:
        path = []
        while n not in path:
            if n == 1:
                return True
            path.append(n)
            square_sum = 0
            while n:
                square_sum += (n % 10)**2
                n //= 10
            n = square_sum

        return False


s = Solution()

inputs = [
    19, #t
    2, #f
    7, #t
]

for i in inputs:
    print(s.isHappy(i))
