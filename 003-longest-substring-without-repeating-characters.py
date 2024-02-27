

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_pos = {}
        start = 0
        maxlen = 0

        for i, ch in enumerate(s):
            if last_pos.get(ch) is not None:
                start = max(start, last_pos[ch] + 1)
            maxlen = max(maxlen, i-start+1)
            last_pos[ch] = i

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