class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        orig, reverse = x, 0
        while x:
            reverse *= 10
            reverse += x % 10
            x /= 10
        return orig == reverse

s = Solution()
s.isPalindrome(1)
