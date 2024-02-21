
from typing import List

class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        # length ~= 10^5, single pass only
        # monotonic stack
        n = len(nums)
        nse = [i for i in range(n)]
        nge = [i for i in range(n)]
        costs[0] = 0
        larger = []
        smaller = []
        jump_costs = [float('inf')] * n
        jump_costs[0] = 0

        for i in range(n):
            while larger and nums[larger[-1]] > nums[i]:
                nse[larger.pop()] = i
            while smaller and nums[smaller[-1]] <= nums[i]:
                nge[smaller.pop()] = i
            larger.append(i)
            smaller.append(i)

        for i in range(n):
            for j in (nse[i], nge[i]):
                jump_costs[j] = min(jump_costs[j], costs[j]+jump_costs[i])

        return jump_costs[-1]



s = Solution()

data = [
    [[3,2,4,4,1], [3,7,6,4,2]],  # 8
    [[0,1,2], [1,1,1]],  # 2
]

for d in data:
    print(s.minCost(*d))
