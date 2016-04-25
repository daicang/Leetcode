# 334-inceasing-triplet-subsequence.py

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3: return False

        start = 0
        minimal = nums[0]
        bound = 0         # Second minimal (must after minimal)
                          
        for i, v in enumerate(nums):
            if v < minimal:
                minimal = v
                continue
            if v > minimal:
                bound = v
                start = i
                break

        if start == 0: return False

        for i in xrange(start, len(nums)):
            v = nums[i]
            if v > bound: return True
            if minimal < v < bound:
                bound = v
            elif v < minimal:
                minimal = v
            
        return False
