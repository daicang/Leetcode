

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def find(i1, i2):
            while i1 >= 0 and i2 < len(s) and s[i1] == s[i2]:
                i1 -= 1
                i2 += 1
            return s[i1+1:i2]

        pali = ''
        for i in range(len(s)):
            l = find(i, i)
            if len(l) > len(pali):
                pali = l
            l = find(i, i+1)
            if len(l) > len(pali):
                pali = l
        return pali
