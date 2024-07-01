

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_pos = {}
        maxlen = 0
        start_idx = 0

        for i, ch in enumerate(s):
            if ch in last_pos:
                start_idx = max(start_idx, last_pos[ch] + 1)
            last_pos[ch] = i
            maxlen = max(maxlen, i - start_idx + 1)

        return maxlen

s = Solution()

data = [
    'abcabcbb', # 3
    'bbbbb', # 1
    "pwwkew", # 3
    'tmmzuxt', # 5
]

for d in data:
    print(s.lengthOfLongestSubstring(d))