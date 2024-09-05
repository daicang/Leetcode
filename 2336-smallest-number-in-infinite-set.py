class SmallestInfiniteSet:

    def __init__(self):
        self.removed = [False] * 2000

    def popSmallest(self) -> int:
        for i in range(1, 2000):
            if not self.removed[i]:
                self.removed[i] = True
                return i

    def addBack(self, num: int) -> None:
        self.removed[num] = False