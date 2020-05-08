from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while high - low > 1:
            mid = (low + high) // 2
            left_ele = nums[mid-1]
            mid_ele = nums[mid]
            right_ele = nums[mid+1]
            # print(left_ele, mid_ele, right_ele)

            if mid_ele > left_ele:
                if mid_ele > right_ele:
                    return mid
                # right > mid > left
                low = mid + 1

            else: # mid < left
                if mid_ele > right_ele:
                    # left > mid > right
                    high = mid - 1
                else:
                    # left > mid, right > mid
                    high = mid - 1

        if nums[low] > nums[high]:
            return low
        return high


s = Solution()

data = [
    [1,2,3,1],
    [1,2,1,3,5,6,4]
]

for d in data:
    print(s.findPeakElement(d))
