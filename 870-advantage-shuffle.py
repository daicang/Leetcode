
from typing import List

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [None] * len(nums2)
        nums1.sort()
        n2 = [(val, i) for i, val in enumerate(nums2)]
        n2.sort(reverse=1)
        low = 0
        high = len(nums1) - 1
        for val, i in n2:
            if val < nums1[high]:
                result[i] = nums1[high]
                high = high - 1
            else:
                result[i] = nums1[low]
                low = low + 1
        return result
