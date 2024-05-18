from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1

        while lo < hi:
            mid = (lo+hi) // 2

            if nums[lo] == target:
                return lo
            if nums[hi] == target:
                return hi
            if nums[mid] == target:
                return mid

            if nums[lo] < nums[mid]:
                if nums[lo] < target < nums[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target < nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid

        assert lo == hi
        if nums[lo] == target:
            return lo
        return -1
