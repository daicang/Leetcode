class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def bisearch(start, end):
            if start == end and target == nums[start]:
                return start
            if start >= end:
                return -1

            half = (start+end) / 2
            midpoint = nums[half]

            if target == nums[start]:
                return start
            if target == nums[end]:
                return end
            if target == midpoint:
                return half

            if midpoint >= nums[start]:
                # First part is in ascending order
                if target > nums[start] and target < midpoint:
                    return bisearch(start+1, half-1)
                else:
                    return bisearch(half+1, end-1)

            else:
                # Second part is in ascending order
                if target > midpoint and target < nums[end]:
                    return bisearch(half+1, end-1)
                else:
                    return bisearch(start+1, half-1)

        return bisearch(0, len(nums)-1)


s = Solution()

inputs = [
    ([4,5,6,7,0,1,2], 0),
]

for input in inputs:
    print s.search(*input)
