class Solution(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        if len(nums) == 1:
            return nums[0] == 1

        def gcd(x, y):
            if 1 in (x, y):
                return 1

            if x < y:
                # Make x >= y
                x, y = y, x

            mod = x%y
            if mod == 0:
                return y
            return gcd(y, mod)

        size = len(nums)
        gcd_val = nums[0]
        for i in range(1, size):
            gcd_val = gcd(gcd_val, nums[i])
            if gcd_val == 1:
                return True

        return False

