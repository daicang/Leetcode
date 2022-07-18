from typing import List

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        tracker = deque()
        for i in range(k):
            elem = nums[i]
            while len(tracker) > 0 and tracker[-1] < elem:
                tracker.pop()
            tracker.append(elem)

        results = []
        end_idx = k-1

        while end_idx < len(nums):
            results.append(tracker[0])

            if end_idx + 1 < len(nums): # prepare for next move
                start_idx = end_idx - k + 1
                if nums[start_idx] == tracker[0]:
                    tracker.popleft()
                next_elem = nums[end_idx+1]
                while len(tracker) > 0 and tracker[-1] < next_elem:
                    tracker.pop()
                tracker.append(next_elem)

            end_idx += 1

        return results

inputs = [
    [[1,3,-1,-3,5,3,6,7], 3],
    [[1], 1],
]

s = Solution()

for i in inputs:
    print(s.maxSlidingWindow(*i))
