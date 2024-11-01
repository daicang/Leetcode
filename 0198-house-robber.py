class Solution:
    def rob(self, nums: List[int]) -> int:
        v_rob, v_norob = 0, 0
        for i, val in enumerate(nums):
            v_rob, v_norob = val+v_norob, max(v_rob, v_norob)

        return max(v_rob, v_norob)
