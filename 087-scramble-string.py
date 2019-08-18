class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        from collections import Counter
        if Counter(s1) != Counter(s2):
            return False

        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False

s = Solution()

inputs = [
    ["great", "rgeat"],
    ["abcde", "caebd"]
]

for i in inputs:
    print s.isScramble(*i)

