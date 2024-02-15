

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            if n < 0:
                n = -n
            idx = n - 1
            if nums[idx] > 0:
                nums[idx] *= -1
        disappeared = []
        for i, n in enumerate(nums):
            if n > 0:
                disappeared.append(i+1)
        return disappeared
