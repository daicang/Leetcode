class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        counter = 0
        for val in nums:
            if val == 0:
                counter = 0
            else:
                counter += 1
                max_len = max(max_len, counter)
        return max_len