class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        val = 1
        for i in range(n-1):
            val *= nums[i]
            result[i+1] *= val

        val = 1
        for i in range(n-1, 0, -1):
            val *= nums[i]
            result[i-1] *= val

        return result
