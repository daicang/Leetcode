from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        moves = 0
        arr = sorted(nums)
        li = 0
        hi = len(arr)-1

        while li < hi:
            moves += arr[hi] - arr[li]
            hi -= 1
            li += 1

        return moves

s = Solution()
inputs = [
    [1,2,3],
    [1,10,2,9],
]

for i in inputs:
    print(s.minMoves2(i))