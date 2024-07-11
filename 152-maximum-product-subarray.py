class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        last_max = last_min = max_p = nums[0]
        for i, n in enumerate(nums):
            if i > 0:
                max_tmp = last_max * n
                min_tmp = last_min * n
                last_max = max(n, max_tmp, min_tmp)
                last_min = min(n, max_tmp, min_tmp)
                max_p = max(max_p, last_max)

        return max_p