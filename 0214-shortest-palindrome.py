


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i = 0
        j = len(s)-1

        while j >= 0:
            if s[j] == s[i]:
                i += 1
            j -= 1

        if i == len(s):
            return s

        no_pali = s[i:]
        return no_pali[::-1] + self.shortestPalindrome(s[:i]) + no_pali


s = Solution()

inputs = [
    "aacecaaa",
    'abcd',
]

for i in inputs:
    print(s.shortestPalindrome(i))
