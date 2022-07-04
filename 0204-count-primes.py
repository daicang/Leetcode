import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        primes = [1] * n
        primes[0] = 0
        primes[1] = 0

        ub = math.ceil(math.sqrt(n))

        for i in range(2, ub+1):
            if primes[i] == 0:
                continue
            j = i * i
            while j < n:
                primes[j] = 0
                j += i

        return sum(primes)


s = Solution()

inputs = [
    0,1,2,10,499979,999983,1000000
]

for i in inputs:
    print(s.countPrimes(i))
