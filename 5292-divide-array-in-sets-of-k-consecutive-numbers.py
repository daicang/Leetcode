
from typing import List

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        nums.sort()

        numbers = []
        counter = []
        count = 0

        for i, n in enumerate(nums):
            count += 1
            # compare next element / tail to add record
            if i == len(nums)-1 or nums[i+1] != n:
                numbers.append(n)
                counter.append(count)
                count = 0

        for i, count in enumerate(counter):
            if count > 0:
                for j in range(i+1, i+k):
                    # check continuity and count
                    if j >= len(counter) or counter[j] < count or numbers[j] != numbers[j-1]+1:
                        return False
                    counter[j] -= count

        return True


data = [
    [[1,2,3,3,4,4,5,6], 4],
]

s = Solution()

for d in data:
    print(s.isPossibleDivide(*d))
