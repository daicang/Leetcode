class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        for i in range(l):
            if i > len(nums)-1:
                break
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                del nums[i+1]
        return len(nums)



s = Solution()
input = [1,1]
print s.removeDuplicates(input)
print input
