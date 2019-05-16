class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1 = sorted(nums1)
        s2 = sorted(nums2)

        result = []
        i1 = i2 = 0

        while i1 < len(s1) and i2 < len(s2):
            if s1[i1] < s2[i2]:
                i1 += 1
            elif s1[i1] > s2[i2]:
                i2 += 1
            else:
                result.append(s1[i1])
                i1 += 1
                i2 += 1
        return result


