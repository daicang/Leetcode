class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nset = set(nums)
        consecutive_count = 0

        for n in nums:
            if n-1 not in nset:
                count = 0
                while n in nset:
                    count += 1
                    n += 1
                consecutive_count = max(consecutive_count, count)

        return consecutive_count

s = Solution()

print s.longestConsecutive([100, 4, 200, 1, 3, 2])

