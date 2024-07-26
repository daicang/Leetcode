class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        arr1 = [0] * 2001
        arr2 = [0] * 2001
        for n in nums1:
            arr1[n+1000] = 1
        for n in nums2:
            arr2[n+1000] = 1
        r1, r2 = [], []
        for i in range(2001):
            if arr1[i] and not arr2[i]:
                r1.append(i-1000)
            elif arr2[i] and not arr1[i]:
                r2.append(i-1000)
        return r1, r2