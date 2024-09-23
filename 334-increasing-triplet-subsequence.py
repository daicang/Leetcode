
from math import inf
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Linear scan
        # Time: O(n), space: O(1)
        fst = sec = inf
        for n in nums:
            if n <= fst:
                fst = n
            elif n <= sec:
                sec = n
            else:
                return True
        return False
