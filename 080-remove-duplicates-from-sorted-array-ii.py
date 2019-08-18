class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0

        l = 0
        last = None
        last_counter = 0
        for r, rval in enumerate(nums):
            if rval == last:
                last_counter += 1
                if last_counter < 3:
                    nums[l] = rval
                    l += 1
            else:
                last_counter = 1
                count += 1
                nums[l] = rval
                l += 1
            last = rval

        return count

