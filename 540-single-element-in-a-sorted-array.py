

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        val = 0
        for n in nums:
            val ^= n
        return val
