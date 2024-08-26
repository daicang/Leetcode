class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Time: O(n)
        # Space: O(1)
        count = 0
        bi = 0
        p = 1

        for i, n in enumerate(nums):
            p *= n
            while p >= k and bi <= i:
                p /= nums[bi]
                bi += 1
            count += i - bi + 1

        return count
