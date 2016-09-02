#!/usr/bin/python

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        size = len(nums1) + len(nums2)
        if size % 2 == 0:
            return (self.getk(nums1[:], nums2[:], size/2)+
                    self.getk(nums1[:], nums2[:], size/2-1))/2.0
        else:
            return self.getk(nums1[:], nums2[:], size/2)
        
    def getk(self, a, b, k):
        if len(a) > len(b): a, b = b, a
        if len(a) <= 2:
            b.extend(a)
            b.sort()
            return b[k]
        if not a: return b[k]
        if k <= 0: return min(a[0], b[0])
        m, n = len(a), len(b)
        if (m+n)/2 >= k:
            if a[m/2] >= b[n/2]:
                return self.getk(a[:m/2+1], b, k)
            else:
                return self.getk(a, b[:n/2+1], k)
        else:
            if a[m/2] >= b[n/2]:
                return self.getk(a, b[n/2:], k - n/2)
            else:
                return self.getk(a[m/2:], b, k - m/2)
                    
# def myfunc(a, b, c):
#     return a, b, c
# print myfunc(1, 2, 4/3)
                
a = [1, 2, 3, 4, 5]
b = [3, 5, 6, 7]
c = []
d = [1]
e = [2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 17, 54, 83]
f = [1, 6, 9, 22, 45, 103, 255, 1024]
g = [1, 2, 2]
h = [1, 2, 3]

s = Solution()
print s.findMedianSortedArrays(a, b)
print s.findMedianSortedArrays(c, d)
print s.findMedianSortedArrays(e, f)
print s.findMedianSortedArrays(g, h)
