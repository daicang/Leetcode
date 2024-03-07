
from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        preSum = [0] * (len(nums) + 1)
        for i, val in enumerate(nums):
            preSum[i + 1] = preSum[i] + val

        def merge_sort(left, right):
            if right - left < 2:
                return 0
            mid = (left + right) // 2
            count = merge_sort(left, mid) + merge_sort(mid, right)

            start = end = mid
            for i in range(left, mid):
                # sum of elems in [i, ei] with ei in [start, end) is in range [lower, upper]
                while start < right and preSum[start] - preSum[i] < lower:
                    start += 1
                while end < right and preSum[end] - preSum[i] <= upper:
                    end += 1
                count += end - start

            arr1 = preSum[left:mid]
            arr2 = preSum[mid:right]

            i1 = i2 = 0
            j = left

            while i1 < len(arr1) and i2 < len(arr2):
                if arr1[i1] < arr2[i2]:
                    preSum[j] = arr1[i1]
                    i1 += 1
                else:
                    preSum[j] = arr2[i2]
                    i2 += 1
                j += 1

            for i in range(i1, len(arr1)):
                preSum[j] = arr1[i]
                j += 1
            for i in range(i2, len(arr2)):
                preSum[j] = arr2[i]
                j += 1
            return count

        return merge_sort(0, len(preSum))


s = Solution()

data = [
    [[2, 5, -1], -2, 2],  # 3
    [[0], 0, 0],  # 1
]

for d in data:
    print(s.countRangeSum(*d))
