class Solution:

    def __init__(self, w: List[int]):
        self.w = []
        s = 0
        for weight in w:
            s += weight
            self.w.append(s)

    def pickIndex(self) -> int:
        val = random.randrange(self.w[-1])
        return bisect.bisect_right(self.w, val)
