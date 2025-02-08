class Solution:
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        n = len(nums)
        max_sum = -inf
        last_sum = -inf
        total_sum = 0

        min_sum = inf
        last_min_sum = inf

        for i, val in enumerate(nums):
            total_sum += val
            last_sum = last_sum + val if last_sum > 0 else val
            max_sum = max(max_sum, last_sum)

            if i > 0 and i < n-1:
                last_min_sum = last_min_sum + val if last_min_sum < 0 else val
                min_sum = min(min_sum, last_min_sum)

        if last_min_sum == inf:
            return max_sum
        return max(max_sum, total_sum - min_sum)

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        n = len(nums)
        max_sum = -inf
        last_sum = -inf

        # normal max subarray sum
        for i, val in enumerate(nums):
            last_sum = last_sum + val if last_sum > 0 else val
            max_sum = max(max_sum, last_sum)

        prefix_sum = [0] * n
        suffix_sum = [0] * n

        # creating prefix/suffix sum

        for i in range(n):
            if i == 0:
                prefix_sum[i] = nums[i]
            else:
                prefix_sum[i] = prefix_sum[i-1] + nums[i]

        for i in range(n-1, -1, -1):
            if i == n-1:
                suffix_sum[i] = nums[i]
            else:
                suffix_sum[i] = nums[i] + suffix_sum[i+1]

        # iterate over prefix sum [0 .. i]
        # find prefix_sum[i] + max(suffix_sum[i+1 .. n-1])

        suffix_max = -inf
        for i in range(n-1, 0, -1):
            suffix_max = max(suffix_max, suffix_sum[i])
            max_sum = max(max_sum, suffix_max + prefix_sum[i-1])

        return max_sum
