from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p_total = 1
        size = len(nums)
        for n in nums:
            p_total *= n

        lefts = [1] * size
        rights = [1] * size
        result = [None] * size

        for i in range(1, size):
            lefts[i] = lefts[i-1] * nums[i-1]
            rights[size-i-1] = rights[size-i] * nums[size-i]

        for i in range(size):
            result[i] = lefts[i] * rights[i]

        return result

s = Solution()
data = [
    [1,2,3,4],
]

for d in data:
    print(s.productExceptSelf(d))

