class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permuations = []

        def backtrack(start):
            if start == len(nums)-1:
                permuations.append(nums[:])
            used = set()
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return permuations


inputs = [
    [2,2,1,1],
]

s = Solution()

for input in inputs:
    print s.permuteUnique(input)
