from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        head = 0
        tail = len(nums) - 1

        if nums[head] < nums[tail]:
            return nums[0]

        # [10,1,10,10,10]
        while head < tail and nums[head] == nums[tail]:
            head += 1

        if nums[head] <= nums[tail]:
            return nums[head]

        while tail - head > 1:
            mid = (head + tail) // 2

            if nums[mid] >= nums[head]:
                head = mid
            else:
                tail = mid

        return min(nums[tail], nums[head])

s = Solution()

data = [
    [3,3,4,4,5,5,1,2,2],
    [0,0,1,1,2],
    [2,2,2,0,1],
    [10,1,10,10,10]
]

for d in data:
    print(s.findMin(d))
