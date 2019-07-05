class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def bisearch_front(start, end):
            if start > end:
                return -1
            if start == end:
                return start if nums[start] == target else -1

            half = (start+end) / 2

            if nums[half] > target:
                return bisearch_front(start, half-1)
            elif nums[half] < target:
                return bisearch_front(half+1, end)
            else:
                if half == 0 or nums[half-1] != target:
                    return half
                else:
                    return bisearch_front(start, half-1)

        front_idx = bisearch_front(0, len(nums)-1)
        if front_idx == -1:
            return -1, -1

        if front_idx == len(nums)-1 or nums[front_idx+1] != target:
            return front_idx, front_idx

        def bisearch_end(start, end):
            assert start <= end
            if start == end:
                assert nums[start] == target
                return start

            half = (start+end) / 2

            if nums[half] > target:
                return bisearch_end(start, half-1)
            else:
                assert nums[half] == target
                if half == len(nums)-1 or nums[half+1] != target:
                    return half
                return bisearch_end(half+1, end)

        return front_idx, bisearch_end(front_idx+1, len(nums)-1)

inputs = [
    [[2, 2], 2],
]

s = Solution()
for input in inputs:
    print input
    print(s.searchRange(*input))

