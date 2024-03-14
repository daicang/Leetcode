
import random
import bisect
class Solution:
    def __init__(self, w: List[int]):
        self.arr = [0] * len(w)
        for i, weight in enumerate(w):
            if i == 0:
                self.arr[i] = weight
            else:
                self.arr[i] = self.arr[i-1] + weight

    def pickIndex(self) -> int:
        weight_val = random.randrange(self.arr[-1])
        return bisect.bisect_right(self.arr, weight_val)
