from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = {}
        stack = []
        arr = nums2[::-1]
        for n in arr:
            while stack and stack[-1] < n:
                stack.pop()
            if stack:
                greater[n] = stack[-1]
            stack.append(n)

        return [greater.get(n, -1) for n in nums1]
