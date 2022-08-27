from typing import List

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def factorize(k, first_factor, first_time=False):
            if first_time:
                factors = []
            else:
                factors = [[k]]
            for i in range(first_factor, k):
                if i*i > k:
                    break
                q, r = divmod(k, i)
                if r == 0:
                    rest_factors = factorize(q, i)
                    for rf in rest_factors:
                        factors.append([i] + rf)

            return factors

        return factorize(n, 2, True)


s = Solution()

inputs = [
    1, 12, 37
]

for i in inputs:
    print(s.getFactors(i))
