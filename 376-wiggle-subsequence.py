class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        wlen = 1  # nums[0]
        last, nums = nums[0], nums[1:]
        for num in nums:
            if num != last:
                if num < last:
                    nextsmall = 1
                else:
                    nextsmall = 0
                break

        for num in nums:
            if num > last:
                if nextsmall:
                    last = max(last, num)
                else:
                    last = num
                    nextsmall = 1
                    wlen += 1
            elif num < last:
                if nextsmall:
                    last = num
                    nextsmall = 0
                    wlen += 1
                else:
                    last = min(last, num)

        return wlen

s = Solution()
print s.wiggleMaxLength([3, 3, 3, 2, 5])
