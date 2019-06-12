class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        prefixes = []
        for i, ch in enumerate(strs[0]):
            for s in strs[1:]:
                if len(s) < i+1 or s[i] != ch:
                    return ''.join(prefixes)
            prefixes.append(ch)
        return ''.join(prefixes)
