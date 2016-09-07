import collections


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        md = collections.defaultdict(int)

        for ch in magazine:
            md[ch] += 1

        for ch in ransomNote:
            md[ch] -= 1

        for v in md.itervalues():
            if v < 0:
                return False
        return True
