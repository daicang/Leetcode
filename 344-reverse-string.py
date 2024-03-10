

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i1 = 0
        i2 = len(s)-1

        while i1 < i2:
            s[i1], s[i2] = s[i2], s[i1]
            i1 += 1
            i2 -= 1
