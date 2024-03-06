# 327-count-of-range-sum.py

from typing import List


class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        def iter(start, end):
            if end - start <= 1: return 0
            mid = (start + end) / 2
            count = iter(start, mid) + iter(mid, end)
            cache = [0] * (end - start)
            j = k = t = mid
            r = 0
            for i in xrange(start, mid):
                while j < end and sum[j] - sum[i] < lower: j += 1
                while k < end and sum[k] - sum[i] <= upper: k += 1
                while t < end and sum[t] < sum[i]:
                    cache[r] = sum[t]
                    t += 1
                    r += 1
                cache[r] = sum[i]
                r += 1
                count += k - j
            for i in xrange(r): sum[start+i] = cache[i]
            return count

        l = len(nums)
        sum = [0]*(l+1)
        for i in xrange(1, l+1): sum[i] = sum[i-1] + nums[i-1]
        return iter(0, l+1)

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        pre_sum = [0] * (len(nums)+1)
        for i, val in enumerate(nums):
            pre_sum[i+1] = pre_sum[i] + val

        def merge_sort(left, right):
            if right - left < 2:
                return 0

            mid = (left + right) // 2
            count = merge_sort(left, mid) + merge_sort(mid, right)

            start = end = mid
            for i in range(mid):
                while start < right and pre_sum[start] - pre_sum[i] < lower:
                    start += 1
                while end < right and pre_sum[end] - pre_sum[i] <= upper:
                    end += 1
                count += end - start

            arr1 = pre_sum[left:mid]
            arr2 = pre_sum[mid:right]
            i1 = i2 = 0
            j = left

            while i1 < len(arr1) and i2 < len(arr2):
                if arr1[i1] < arr2[i2]:
                    pre_sum[j] = arr1[i1]
                    i1 += 1
                else:
                    pre_sum[j] = arr2[i2]
                    i2 += 1
                j += 1

            for i in range(i1, len(arr1)):
                pre_sum[j] = arr1[i]
                j += 1
            for i in range(i2, len(arr2)):
                pre_sum[j] = arr2[i]
                j += 1

            return count

        return merge_sort(0, len(pre_sum))


s = Solution()

data = [
    [[2, 5, -1], -2, 2],
]

for d in data:
    print(s.countRangeSum(*d))
