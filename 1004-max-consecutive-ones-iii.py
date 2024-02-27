
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        maxlen = 0

        zeros = 0
        ones = 0

        for i, n in enumerate(nums):
            if n == 0:
                zeros += 1
            else:
                ones += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            maxlen = max(maxlen, i-left+1)

        return maxlen


s = Solution()
print(s.longestOnes([0,0,0,1], 4))
