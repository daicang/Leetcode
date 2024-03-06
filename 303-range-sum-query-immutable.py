

class NumArray:

    def __init__(self, nums: List[int]):
        self.sum_arr = []
        for i, n in enumerate(nums):
            if i == 0:
                self.sum_arr.append(n)
            else:
                self.sum_arr.append(n + self.sum_arr[-1])

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sum_arr[right]
        else:
            return self.sum_arr[right] - self.sum_arr[left-1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)