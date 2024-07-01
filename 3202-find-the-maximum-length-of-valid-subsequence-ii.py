from collections import defaultdict

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # remainders[r][n], remainder is r, next elem is n
        # r, n both [0, k-1]
        counter = []
        for _ in range(k):
            counter.append([0] * k)

        maxlen = 0
        for n in nums:
            n = n % k
            for r in range(k):
                other = ((k+r) - n) % k
                counter[r][other] = counter[r][n] + 1
                maxlen = max(maxlen, counter[r][other])

        return maxlen
