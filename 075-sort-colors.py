class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def find_first(target):
            i = 0
            while i < len(nums):
                if nums[i] == target:
                    return i
                i += 1
            return None

        for i, val in enumerate(nums):
            if val < 2:
                j = find_first(2)
                if j is None:
                    break
                if j < i:
                    nums[i], nums[j] = nums[j], nums[i]

        for i, val in enumerate(nums):
            if val < 1:
                j = find_first(1)
                if j is None:
                    break
                if j < i:
                    nums[i], nums[j] = nums[j], nums[i]



s = Solution()
l = [2,0,2,1,1,0]

s.sortColors(l)
print l

