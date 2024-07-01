class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        partity = None
        for i, n in enumerate(nums):
            if i > 0:
                if n % 2 == parity:
                    return False
            parity = n % 2
        return True
