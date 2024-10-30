class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        # index of bitree starts from 1
        self.bitree = [0] * (self.n+1)
        for i, val in enumerate(nums):
            self._update(i, val)

    def _update(self, i, delta):
        i += 1
        while i <= self.n:
            self.bitree[i] += delta
            i += i & (-i)

    def update(self, index: int, val: int) -> None:
        self._update(index, val-self.nums[index])
        self.nums[index] = val

    def getSum(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.bitree[i]
            lsb = i & (-i)
            i -= lsb
        return s

    def sumRange(self, left: int, right: int) -> int:
        return self.getSum(right) - self.getSum(left-1)




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)