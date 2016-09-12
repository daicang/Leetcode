class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        idx = 0
        lt = len(t)
        for ch in s:
            while idx < lt:
                if t[idx] == ch:
                    idx += 1
                    break
                idx += 1
            else:
                return False
        return True
