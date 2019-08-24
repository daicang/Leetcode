class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subs = [[],]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                # l = size of subset by adding nums[i-1]
                l = len(subs)

            begin = len(subs) - l
            end = len(subs)
            for j in range(begin, end):
                subs.append(subs[j]+[nums[i]])
        return subs

s = Solution()

print s.subsetsWithDup([1,2,2])
