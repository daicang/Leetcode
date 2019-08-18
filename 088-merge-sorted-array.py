class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        i1 = i2 = 0
        nums1[m:] = []

        while i1 < len(nums1) and i2 < n:
            if nums1[i1] < nums2[i2]:
                i1 += 1
                continue
            # nums1[i1] >= nums2[i2]
            print i1
            nums1.insert(i1, nums2[i2])
            i2 += 1

        if i2 < n:
            nums1.extend(nums2[i2:])
        # print nums1


s = Solution()
l = [1,2,3,0,0,0]

# s.merge(l, 3, [2,5,6], 3)

s.merge([4,0,0,0,0,0], 1, [1,2,3,5,6], 5)
