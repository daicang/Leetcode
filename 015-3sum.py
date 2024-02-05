
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def two_sum(start, target):
            l = start
            r = len(nums)-1
            ret = []
            while l < r:
                s = nums[l] + nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    ret.append([nums[l], nums[r]])
                    while l < r and nums[l+1] == nums[l]:
                        l += 1
                    while l < r and nums[r-1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1

            return ret

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            r = two_sum(i+1, 0-n)
            for s in r:
                s.append(n)
                result.append(s)

        return result
