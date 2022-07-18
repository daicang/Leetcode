

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            if n in d:
                return True
        return False
