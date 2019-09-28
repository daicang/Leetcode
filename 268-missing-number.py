class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = len(nums)

        for i, n in enumerate(nums):
            xor ^= n
            xor ^= i

        return xor

inputs = [
    [0],
    [1],
    [3,0,1],
    [9,6,4,2,3,5,7,0,1]
]

s = Solution()
for i in inputs:
    print s.missingNumber(i)
