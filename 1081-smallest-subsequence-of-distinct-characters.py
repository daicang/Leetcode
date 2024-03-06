

from collections import Counter

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        if not s:
            return s

        counter = Counter(s)
        stack = []
        in_stack = {}

        for ch in s:
            counter[ch] -= 1
            if in_stack.get(ch):
                continue

            while stack and stack[-1] >= ch and counter[stack[-1]] > 0:
                pop_ch = stack.pop()
                in_stack[pop_ch] = False
            stack.append(ch)
            in_stack[ch] = True

        return ''.join(stack)


s = Solution()

data = [
    "bcabc",  # abc
    "cbacdcbc", # acdb
    "bcbcbcababa", # bca
]

for d in data:
    print(s.smallestSubsequence(d))
