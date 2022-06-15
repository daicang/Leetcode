from typing import List

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        largest = 0

        for i in range(len(flips)):
            ele = flips[i]
            largest = max(ele, largest)
            if largest == i+1:
                count += 1

        return count


s = Solution()
inputs = [
    [3,2,4,1,5],  # 2
    [4,1,2,3]  # 1
]

for i in inputs:
    print(s.numTimesAllBlue(i))
