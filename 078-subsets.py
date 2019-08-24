class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from copy import copy
        subs = []

        def backtrack(i, l):
            if i == len(nums):
                subs.append(copy(l))
                return
            backtrack(i+1, l)
            l.append(nums[i])
            backtrack(i+1, l)
            l.pop()

        backtrack(0, [])
        return subs

s = Solution()

print s.subsets([1,2,3])
