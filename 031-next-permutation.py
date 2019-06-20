class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        def quicksort(arr, begin, end):
            if end <= begin:
                return

            pivot = arr[end]
            # ..(<=pivot) <smaller_idx(first bigger)> ..(>pivot)
            # smaller-index points to first element bigger than pivot
            # bigger-index points to next element to compare with pivot
            smaller_idx, bigger_idx = begin, begin

            while bigger_idx < end:
                if arr[bigger_idx] < pivot:
                    arr[smaller_idx], arr[bigger_idx] = arr[bigger_idx], arr[smaller_idx]
                    smaller_idx += 1
                bigger_idx += 1
            arr[smaller_idx], arr[end] = pivot, arr[smaller_idx]
            quicksort(arr, begin, smaller_idx-1)
            quicksort(arr, smaller_idx+1, end)

        if len(nums) < 2:
            return nums

        # ...num[i], num[i+1], ...
        # iterate i in descending order, find first num[i] < num[i+1]

        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                break
        else:
            # No next permutation, sort and return
            quicksort(nums, 0, len(nums)-1)
            return

        # Find minimal num[j] > num[i] for j in [i+1, len(nums)-1],
        # swap num[j] with num[i]

        for j in range(i+1, len(nums)):
            if j == len(nums)-1 or nums[j+1] <= nums[i]:
                # print 'swap nums[%s]=%s with nums[%s]=%s' % (i, nums[i], j, nums[j])
                nums[i], nums[j] = nums[j], nums[i]
                break

        # Sort nums[i+1, ..]

        # print 'sort %s' % nums[i+1:len(nums)-1]
        quicksort(nums, i+1, len(nums)-1)

s = Solution()
inputs = [
    # [1,2,3],  # 1 3 2
    # [3,2,1],  # 1 2 3
    # [1,1,5],  # 1 5 1
    [1,2]  # 2 1
]
import copy
for input in inputs:
    raw_input = copy.copy(input)
    s.nextPermutation(input)
    print '%s -> %s' % (raw_input, input)
