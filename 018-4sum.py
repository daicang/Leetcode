
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

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

        nums.sort()
        result = []
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                t = target - n - nums[j]
                two = two_sum(j+1, t)
                for s in two:
                    result.append([n, nums[j], *s])

        return result
