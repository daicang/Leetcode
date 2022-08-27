

class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.outer_idx = 0
        self.inner_idx = 0

    def next(self) -> int:
        while len(self.vec[self.outer_idx]) == 0:
            self.outer_idx += 1
            self.inner_idx = 0
        val = self.vec[self.outer_idx][self.inner_idx]
        self.inner_idx += 1
        if self.inner_idx == len(self.vec[self.outer_idx]):
            self.outer_idx += 1
            self.inner_idx = 0

        return val

    def hasNext(self) -> bool:
        oi = self.outer_idx
        while oi < len(self.vec):
            if len(self.vec[oi]) > 0:
                return True
            oi += 1
        return False



# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()