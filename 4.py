#!/usr/bin/python

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        def getk(a, b, k):
            m, n = len(a), len(b)
            if m == 0: return b[k]
            if n == 0: return a[k]
            if k <= 0: return min(a[0], b[0])
            if (m+n)/2 >= k:
                if a[m/2] >= b[n/2]:
                    return getk(a[:m/2+1], b, k)
                else:
                    return getk(a, b[:n/2+1], k)
            else:
                if a[m/2] >= b[n/2]:
                    return getk(a, b[n/2:], k - n/2)
                else:
                    return getk(a[m/2:], b, k - m/2)
            
        size = len(nums1) + len(nums2)
        if size % 2 == 0:
            return (getk(nums1, nums2, size/2)+getk(nums1, nums2, size/2-1))/2.0
        else:
            return getk(nums1, nums2, size/2)
                
a = [1, 2, 3, 4, 5]
b = [3, 5, 6, 7]
c = []
d = [1]
e = [2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 17, 54, 83]
f = [1, 6, 9, 22, 45, 103, 255, 1024]

s = Solution()
print s.findMedianSortedArrays(a, b)
print s.findMedianSortedArrays(c, d)
print s.findMedianSortedArrays(e, f)
