class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        f, b = 0, 0
        zeros = 0
        maxcount = 0

        for f in range(n):
            if nums[f] == 0:
                zeros += 1
                if zeros > 1:
                    while nums[b] != 0:
                        b += 1
                    # skip one 0
                    b += 1
                    zeros -= 1

            l = f-b+1
            maxcount = max(maxcount, l-1)

        return maxcount
