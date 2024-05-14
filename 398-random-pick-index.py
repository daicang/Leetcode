import random
from collections import defaultdict

class Solution:

    def __init__(self, nums: List[int]):
        self.index = defaultdict(list)
        for i, n in enumerate(nums):
            self.index[n].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.index[target])

        # Reservoir sampling
        # ret = -1
        # count = 0
        # for i, n in enumerate(self.nums):
        #     if n == target:
        #         count += 1
        #         if random.random() < 1/count:
        #             ret = i
        # return ret
