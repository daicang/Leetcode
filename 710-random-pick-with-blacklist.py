
import random
from typing import List

class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        # 1,2,3,[4],5, 6
        # 1,2,3, 6 ,5,|4
        #           ^last_idx
        self.index = {}
        blacks = set(blacklist)
        self.size = n - len(blacklist)
        last_idx = n - 1
        for b in blacklist:
            if b < self.size:
                while last_idx in blacks:
                    last_idx -= 1
                self.index[b] = last_idx
                last_idx -= 1

    def pick(self) -> int:
        n = random.randint(0, self.size-1)
        if n in self.index:
            return self.index[n]
        return n



# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()