class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        permutations = []
        def backtrack(first):
            # In-place backtracking
            if first == len(nums)-1:
                permutations.append(nums[:])
                return

            for i in range(first, len(nums)):
                nums[i], nums[first] = nums[first], nums[i]
                backtrack(first+1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack(0)
        return permutations
