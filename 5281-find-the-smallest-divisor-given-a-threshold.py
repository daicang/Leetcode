class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        import math
        left = 1
        right = max(nums)

        def solve(divisor):
            divisor = float(divisor)
            result = 0
            for num in nums:
                result += math.ceil(num / divisor)
            return result

        while left < right:
            mid = (left + right) / 2
            val = solve(mid)
            # print val
            if val > threshold:
                left = mid + 1
            else:
                right = mid

        return left


s = Solution()

data = [
    [[1,2,5,9], 6],
    [[2,3,5,7,11], 11],
    [[19], 5],
]

for d in data:
    print s.smallestDivisor(*d)
