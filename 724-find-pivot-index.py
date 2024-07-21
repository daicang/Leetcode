class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        snums = []  # prefix sums
        s = 0
        for n in nums:
            snums.append(s)
            s += n
        total = snums[-1] + nums[-1]
        for i, val in enumerate(snums):
            if val == (total-nums[i]) / 2:
                return i
        return -1