class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        plain = [ch.lower() for ch in s if ch.isalnum()]
        l = len(plain)
        for i in range(l/2):
            if plain[i] != plain[l-1-i]:
                return False
        return True

