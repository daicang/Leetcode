class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True

        jump = 0
        current_bound = next_bound = nums[0]
        i = 1

        while True:
            jump += 1
            if current_bound >= len(nums)-1:
                return True

            while i <= current_bound:
                next_bound = max(next_bound, i+nums[i])
                i += 1

            if next_bound <= current_bound:
                return False

            current_bound = next_bound