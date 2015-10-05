#!/usr/bin/python

class Solution(object):
    def longestPalindrome(self, s):
        # ret[0]: begin index, ret[1]: substring length
        ret = [0] * 2
        def findpali(a, i, j, arr):
            while i >= 0 and j < len(a) and a[i] == a[j]:
                i = i - 1
                j = j + 1
            if j - i - 1 > ret[1]:
                ret[1] = j - i - 1
                ret[0] = i + 1
        size = len(s)
        if size < 2: return s
        for i in range(size):
            findpali(s, i, i, ret)
            findpali(s, i, i+1, ret)
        return s[ret[0]:ret[0]+ret[1]]

s = Solution()
str1 = "b"
str2 = "aa"
str3 = "abaccd"
str4 = "abb"

print s.longestPalindrome(str1)
print s.longestPalindrome(str2)
print s.longestPalindrome(str3)
print s.longestPalindrome(str4)
