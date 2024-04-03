from typing import List

class Solution:
    def quicksort(self, nums, lower, upper):
        if lower >= upper:
            return

        # tweak to fix TLE
        mid = (lower + upper) // 2
        nums[mid], nums[upper] = nums[upper], nums[mid]

        def partition(lower, upper):
            pivot = nums[upper]
            i = lower
            # .. [i=first greater] .. [j=to compare] .. [last=pivot]
            # .. [i=pivot] .. [all greater]
            # return i
            for j in range(i, upper):
                if nums[j] < pivot:
                    # if current < pivot, move to pos i(switch) and incr i
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[upper] = nums[upper], nums[i]
            return i

        i = partition(lower, upper)
        self.quicksort(nums, lower, i-1)
        self.quicksort(nums, i+1, upper)

    def mergesort(self, nums, lower, upper):
        if upper <= lower:
            return

        mid = (lower+upper) // 2
        self.mergesort(nums, lower, mid)
        self.mergesort(nums, mid+1, upper)

        arr1 = nums[lower:mid+1]
        arr2 = nums[mid+1:upper+1]
        i1 = i2 = 0
        i = lower

        # copy and merge
        while i1 < len(arr1) and i2 < len(arr2):
            if arr1[i1] < arr2[i2]:
                nums[i] = arr1[i1]
                i1 += 1
            else:
                nums[i] = arr2[i2]
                i2 += 1
            i += 1

        while i1 < len(arr1):
            nums[i] = arr1[i1]
            i1 += 1
            i += 1

        while i2 < len(arr2):
            nums[i] = arr2[i2]
            i2 += 1
            i += 1

    def sortArray(self, nums: List[int]) -> List[int]:
        # self.quicksort(nums, 0, len(nums)-1)
        self.mergesort(nums, 0, len(nums)-1)
        return nums



s = Solution()

data = [
    [5,2,3,1],
    [5,1,1,2,0,0],
]

for d in data:
    print(s.sortArray(d))
