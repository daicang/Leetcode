from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        from collections import Counter, defaultdict
        c = Counter(p)
        results = []

        start_idx = 0
        end_idx = 0
        counter = defaultdict(int)
        for end_idx in range(len(p)):
            counter[s[end_idx]] += 1

        while True:
            if counter == c:
                results.append(start_idx)
            counter[s[start_idx]] -= 1
            if counter[s[start_idx]] == 0:
                del counter[s[start_idx]]

            start_idx += 1
            end_idx += 1
            if end_idx >= len(s):
                break
            counter[s[end_idx]] += 1

        return results

s = Solution()

data = [
    ["cbaebabacd", "abc"],
    ["abab", "ab"]
]

for d in data:
    print(s.findAnagrams(*d))
