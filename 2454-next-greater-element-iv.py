
import heapq
from typing import List


class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        sec_greater_elems = [-1] * len(nums)
        stack = []
        h = []

        for i, n in enumerate(nums):
            while h and h[0][0] < n:
                _, idx = heapq.heappop(h)
                sec_greater_elems[idx] = n
            while stack and stack[-1][0] < n:
                # add (value, idx) to heap
                heapq.heappush(h, stack.pop())
            stack.append((n, i))
        return sec_greater_elems


s = Solution()

data = [
    [2,4,0,9,6],
]

for d in data:
    print(s.secondGreaterElement(d))
