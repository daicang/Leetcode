
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0

        def merge_sort(left, right):
            nonlocal count
            if right - left < 2:
                return
            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid, right)

            arr1 = nums[left:mid]
            arr2 = nums[mid:right]

            j = 0
            for i in range(len(arr1)):
                while j < len(arr2) and arr2[j] * 2 < arr1[i]:
                    j += 1
                count += j

            i1 = i2 = 0
            j = left

            while i1 < len(arr1) and i2 < len(arr2):
                if arr1[i1] < arr2[i2]:
                    nums[j] = arr1[i1]
                    i1 += 1
                else:
                    nums[j] = arr2[i2]
                    i2 += 1
                j += 1

            for i in range(i1, len(arr1)):
                nums[j] = arr1[i]
                j += 1
            for i in range(i2, len(arr2)):
                nums[j] = arr2[i]
                j += 1

        merge_sort(0, len(nums))
        return count


s = Solution()

data = [
    [1,3,2,3,1],  # 2
    [2,4,3,5,1],  # 3
    [2147483647,2147483647,-2147483647,-2147483647,-2147483647,2147483647], # 9
]

for d in data:
    print(s.reversePairs(d))
