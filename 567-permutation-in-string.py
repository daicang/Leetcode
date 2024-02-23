
from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        counter = defaultdict(int)
        for ch in s1:
            counter[ch] -= 1

        fi = 0
        bi = 0
        n = len(s1)

        while fi < len(s2):
            val = s2[fi]
            counter[val] += 1
            if counter[val] == 0:
                del counter[val]
            fi += 1
            if fi - bi > n:
                val = s2[bi]
                counter[val] -= 1
                if counter[val] == 0:
                    del counter[val]
                bi += 1
            if len(counter) == 0:
                return True

        return False
