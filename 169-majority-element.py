from typing import List

class Solution:
    def majorityElement1(self, nums: List[int]) -> int:
        def quick_sort(low, high):
            if high <= low:
                return
            pivot = nums[high]
            # i1 is index of first element > pivot
            i1 = low
            i2 = low
            while i2 < high:
                if nums[i2] <= pivot:
                    nums[i1], nums[i2] = nums[i2], nums[i1]
                    i1 += 1
                i2 += 1
            nums[i1], nums[high] = nums[high], nums[i1]
            quick_sort(low, i1-1)
            quick_sort(i1+1, high)

        quick_sort(0, len(nums)-1)
        # print(nums)
        return nums[len(nums)//2]

    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]


s = Solution()

data = [
    [3,2,3],
    [2,2,1,1,1,2,2]
]

for d in data:
    print(s.majorityElement(d))
