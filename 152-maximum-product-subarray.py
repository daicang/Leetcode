from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_arr = [None] * len(nums)
        min_arr = [None] * len(nums)

        for i, n in enumerate(nums):
            if i == 0:
                max_arr[0] = n
                min_arr[0] = n
                continue

            if n >= 0:
                max_arr[i] = max(n, n * max_arr[i-1])
                min_arr[i] = min(n, n * min_arr[i-1])
            else:
                max_arr[i] = max(n, n * min_arr[i-1])
                min_arr[i] = min(n, n * max_arr[i-1])

        return max(max_arr)

s = Solution()

data = [
    [2,3,-2,4],
    [-2, 0, -1]
]

for d in data:
    print(s.maxProduct(d))

