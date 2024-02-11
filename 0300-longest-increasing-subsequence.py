import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

    def lengthOfLIS_bisearch(self, nums: List[int]) -> int:
        lis = []
        for n in nums:
            index = bisect.bisect_left(lis, n)
            if index < len(lis):
                lis[index] = n
            else:
                lis.append(n)
        return len(lis)