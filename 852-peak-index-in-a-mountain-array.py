class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo, hi = 0, len(arr)-1

        while lo < hi:
            mid = (lo+hi) // 2
            val = arr[mid]
            left = arr[mid-1]
            right = arr[mid+1]

            if left < val < right:
                lo = mid
            elif left > val > right:
                hi = mid
            else:
                return mid

        return -1
