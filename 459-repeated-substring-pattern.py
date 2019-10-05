class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return (s+s).find(s, 1) != len(s)

s = Solution()

inputs = [
    'abab', 'aba', 'abcabcabc'
]

for i in inputs:
    print s.repeatedSubstringPattern(i)

