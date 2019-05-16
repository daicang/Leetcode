class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sliding window
        max_len = 0

        li = 0
        ri = 0
        l = 0
        inserted = False

        for ri, rval in enumerate(nums):
            if rval == 1:
                l += 1
                max_len = max(max_len, l)
            else:
                if not inserted:
                    inserted = True
                    l += 1
                    max_len = max(max_len, l)
                else:
                    while nums[li] == 1:
                        li += 1
                    li += 1
                    l = ri-li+1
                    max_len = max(max_len, l)
        return max_len