class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def bisearch(start, end):
            if start == end and target == nums[start]:
                return True
            if start >= end:
                return False

            mid_idx = (start+end) / 2
            mid_val = nums[mid_idx]

            if target in (nums[start], nums[end], mid_val):
                return True

            if mid_val > nums[start]:
                # First part is in ascending order
                if target > nums[start] and target < mid_val:
                    return bisearch(start+1, mid_idx-1)
                else:
                    return bisearch(mid_idx+1, end-1)

            elif mid_val < nums[start]:
                # Second part is in ascending order
                if target > mid_val and target < nums[end]:
                    return bisearch(mid_idx+1, end-1)
                else:
                    return bisearch(start+1, mid_idx-1)

            else:
                # Can't determine the break points locates at which part
                return bisearch(mid_idx+1, end-1) or bisearch(start+1, mid_idx-1)


        return bisearch(0, len(nums)-1)