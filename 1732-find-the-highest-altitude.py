class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxa = 0
        s = 0
        for g in gain:
            s += g
            maxa = max(maxa, s)
        return maxa