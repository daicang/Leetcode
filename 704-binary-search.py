class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo+hi) // 2
            val = nums[mid]
            if val == target:
                return mid
            elif target < val:
                hi = mid-1
            else:
                lo = mid+1
        return -1
