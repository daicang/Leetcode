class Solution:
    def titleToNumber(self, s: str) -> int:
        def chtoi(ch):
            return ord(ch) - ord('A') + 1

        result = 0
        for ch in s:
            result *= 26
            result += chtoi(ch)
        return result

s = Solution()

inputs = [
    'AB',
    'ZY'
]

for input in inputs:
    print(s.titleToNumber(input))