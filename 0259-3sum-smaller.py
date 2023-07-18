
from typing import List

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0

        for i in range(len(nums)-1, 1, -1):
            t1 = target - nums[i]
            # Find j, k in [0, i-1] s.t. nums[j]+nums[k] < t

            last_k = 0
            for j in range(i-1, 0, -1):
                if last_k == j:
                    count += j
                    last_k = j-1
                    continue

                t2 = t1 - nums[j]

                count += last_k+1
                for k in range(last_k, j):
                    if nums[k] >= t2:
                        break
                    count += 1
                last_k = k
                    # print(nums[i], nums[j], nums[k])

        return count

inputs = [
    [[-2,0,1,3], 2], # 2
    [[3,1,0,-2], 4], # 4
    [[], 0],
    [[0], 0],
]

s = Solution()
for i in inputs:
    print(s.threeSumSmaller(*i))
