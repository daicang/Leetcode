class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        up = True
        for i, val in enumerate(nums):
            if i == 0:
                continue
            if up:
                if val < nums[i-1]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
            else:
                if val > nums[i-1]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
            up = not up
