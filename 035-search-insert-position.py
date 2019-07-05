class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def bisearch(start, end):
            if start == end:
                return start if target <= nums[start] else start+1

            half = (start+end) / 2

            if nums[half] == target:
                return half
            if nums[half] < target:
                assert half+1 <= end
                return bisearch(half+1, end)
            else:
                if half-1 < start:
                    if target <= nums[start]:
                        return start
                    else:
                        return half
                return bisearch(start, half-1)

        return bisearch(0, len(nums)-1)


s = Solution()
inputs = [
    [[1,3,5,6], 7],
    [[1,3,5,6], 2]
]
for input in inputs:
    print(s.searchInsert(*input))
