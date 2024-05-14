
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        for i, n in enumerate(nums):
            result = result ^ i
            result = result ^ n
        result = result ^ len(nums)
        return result
