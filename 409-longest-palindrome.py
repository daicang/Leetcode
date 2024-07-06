
from collections import defaultdict, Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        maxlen = 0
        has_odd = False

        for val in counter.values():
            if val % 2 == 0:
                maxlen += val
            else:
                maxlen += val - 1
                has_odd = True

        if has_odd:
            maxlen += 1

        return maxlen
