

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        cs = Counter(s)
        ct = Counter(t)

        count = 0
        for ch, c1 in cs.items():
            if ch not in ct:
                count += c1
            elif c1 > ct[ch]:
                count += c1 - ct[ch]

        for ch, c2 in ct.items():
            if ch not in cs:
                count += c2
            elif c2 > cs[ch]:
                count += c2 - cs[ch]

        return int(count / 2)


s = Solution()
data = [
    ["bab", "aba"],
    ["leetcode", "practice"],
    ["anagram", "mangaar"],
    ["xxyyzz", "xxyyzz"],
    ["friend", "family"]
]

for d in data:
    print(s.minSteps(*d))

