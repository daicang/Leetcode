from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        smallest = nums[0]
        moves = 0
        for val in nums:
            moves += val - smallest

        return moves


s = Solution()
inputs = [
    [1,2,3],
    [1,1,1],
    [1,1,100],
]
for i in inputs:
    print(s.minMoves(i))