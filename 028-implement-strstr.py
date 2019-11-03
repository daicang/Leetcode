class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # KMP algorithm

        def compute_lps(s):
            # Longest prefix given suffixpa
            prefix_len = 0
            lps = [0] * len(s)
            i = 1
            while i < len(s):
                if s[i] == s[prefix_len]:
                    # Index starts at 0, s[prefix_len] is the (prefix_len+1) element
                    prefix_len += 1
                    lps[i] = prefix_len
                    i += 1
                else:
                    if prefix_len != 0:
                        prefix_len = lps[prefix_len-1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps


        if not needle:
            return 0

        lps = compute_lps(needle)
        str_i, pattern_i = 0, 0

        while str_i < len(haystack):
            if haystack[str_i] == needle[pattern_i]:
                str_i += 1
                pattern_i += 1

            if pattern_i == len(needle):
                return str_i - pattern_i

            if str_i < len(haystack) and haystack[str_i] != needle[pattern_i]:
                if pattern_i != 0:
                    pattern_i = lps[pattern_i-1]
                else:
                    str_i += 1

        return -1


s = Solution()

inputs = [
    ("mississippi", "issip")
]

for input in inputs:
    print(s.strStr(*input))

