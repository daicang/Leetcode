# Fisher-Yates shuffle

from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.arr = nums[:]
        self.n = len(nums)

    def reset(self) -> List[int]:
        return self.nums


    def shuffle(self) -> List[int]:
        for i in range(self.n):
            j = random.randint(0, i)
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        return self.arr



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()