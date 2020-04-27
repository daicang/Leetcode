from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        head = 0
        tail = len(nums) - 1

        while True:
            mid = (head + tail) // 2
            if mid == head:
                break

            if nums[mid] > nums[head]:
                head = mid
            else:
                tail = mid

        return nums[tail]

s = Solution()

data = [
    [3,4,5,1,2],
    [0, 1, 2]
]

for d in data:
    print(s.findMin(d))
