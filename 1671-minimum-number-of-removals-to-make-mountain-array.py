class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        # Find left/right LIS
        n = len(nums)
        lpath = [0] * n  # Longest increasing seq from left
        rpath = [0] * n  # Longest increasing seq from right

        lis = []
        for i in range(n):
            j = bisect.bisect_left(lis, nums[i])
            lpath[i] = j
            if j < len(lis):
                lis[j] = nums[i]
            else:
                lis.append(nums[i])

        lis = []
        for i in range(n-1, -1, -1):
            j = bisect.bisect_left(lis, nums[i])
            rpath[i] = j
            if j < len(lis):
                lis[j] = nums[i]
            else:
                lis.append(nums[i])

        max_mountain = 0
        for i in range(n):
            if lpath[i] > 0 and rpath[i] > 0:
                max_mountain = max(max_mountain, lpath[i] + rpath[i] + 1)

        return n - max_mountain
