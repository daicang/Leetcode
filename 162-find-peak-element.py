class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while r - l > 1:
            mid = (l+r) // 2
            if nums[mid] > nums[mid-1]:
                if nums[mid] > nums[mid+1]:
                    return mid
                l = mid+1
            else:
                # nums[mid] < nums[mid-1]
                r = mid-1

        return l if nums[l] > nums[r] else r
