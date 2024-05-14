
class Solution:
    def preimageSizeFZF(self, k: int) -> int:

        def get_zeros(n):
            count = 0
            while n > 0:
                n //= 5
                count += n
            return count

        def atmost_k(k):
            left = 0
            right = 5*k+4

            while left <= right:
                mid = (left+right) // 2
                count = get_zeros(mid)
                if count <= k:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        return atmost_k(k) - atmost_k(k-1)


s = Solution()

data = [
    0, 5, 3
]

for d in data:
    print(s.preimageSizeFZF(d))
