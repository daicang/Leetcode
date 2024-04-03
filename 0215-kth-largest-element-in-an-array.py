from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def find(lower, upper, k):
            # find smallest element at index k (element is (k+1)th smallest)
            pivot = nums[upper]
            i = lower
            # optimize: count same element as pivot
            pivot_counter = 0
            for j in range(lower, upper):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                elif nums[j] == pivot:
                    pivot_counter += 1
            nums[i], nums[upper] = nums[upper], nums[i]

            if i <= k <= i+pivot_counter:
                return pivot
            if i > k:
                return find(lower, i-1, k)
            else:
                # the index remains the same
                return find(i+1, upper, k)

        # kth largest elem has n-k elem smaller
        # so it is (n-k+1)th smallest, indexed at n-k
        return find(0, len(nums)-1, len(nums)-k)

# time: O(N) - O(N^2)
# space: O(1)

s = Solution()

inputs = [
    [[3,2,1,5,6,4], 2], # 5
    [[3,2,3,1,2,4,5,5,6], 4], # 4
]

for i in inputs:
    print(s.findKthLargest(*i))
