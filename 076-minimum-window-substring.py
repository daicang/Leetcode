
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        counter = Counter(t)
        counter_s = {k: 0 for k in counter.keys()}
        avail = 0
        window = None

        for i, ch in enumerate(s):
            if ch not in counter:
                continue
            counter_s[ch] += 1
            if counter_s[ch] == counter[ch]:
                avail += 1

            if avail == len(counter):
                # increase left
                for l in range(left, i+1):
                    ch = s[l]
                    if ch not in counter:
                        continue
                    if counter_s[ch] > counter[ch]:
                        counter_s[ch] -= 1
                    else:
                        left = l
                        break

                if window is None or i-left+1 < len(window):
                    window = s[left:i+1]

        return '' if window is None else window


s = Solution()

inputs = [
    ['ADOBECODEBANC', 'ABC']
]

for i in inputs:
    print(s.minWindow(*i))
