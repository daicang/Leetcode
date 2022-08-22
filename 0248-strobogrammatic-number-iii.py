
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        reversible = {
            0: 0,
            1: 1,
            6: 9,
            8: 8,
            9: 6,
        }

        s_nums = []

        for l in range(len(low), len(high)+1):
