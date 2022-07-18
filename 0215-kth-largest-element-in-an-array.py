from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return heapq.nlargest(k, nums)[-1]

        pivot_idx = 0
        pivot = nums[pivot_idx]
        ri = len(nums)-1

        while pivot_idx < ri:
            val = nums[ri]
            if val > pivot:
                ri -= 1
                continue
            pivot_idx += 1
            nums[ri] = nums[pivot_idx]
            nums[pivot_idx] = pivot
            nums[pivot_idx-1] = val

        pivot_rank = len(nums) - pivot_idx
        if pivot_rank == k:
            return nums[pivot_idx]

        if pivot_rank > k:
            return self.findKthLargest(nums[pivot_idx+1:], k)

        return self.findKthLargest(nums[:pivot_idx], k-pivot_rank)


s = Solution()

inputs = [
    [[3,2,1,5,6,4], 2], # 5
    [[3,2,3,1,2,4,5,5,6], 4], # 4
]

for i in inputs:
    print(s.findKthLargest(*i))
