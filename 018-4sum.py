class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []

        nums.sort()
        sums = []

        last1 = None
        # From largest down to smallest
        for i1 in range(3, len(nums))[::-1]:
            if nums[i1] * 4 < target:
                break
            if nums[i1] == last1:
                continue
            last1 = nums[i1]
            left1 = target - nums[i1]

            last2 = None
            for i2 in range(2, i1)[::-1]:
                if nums[i2] * 3 < left1:
                    break
                if nums[i2] == last2:
                    continue
                last2 = nums[i2]
                left2 = left1 - nums[i2]

                last3 = None
                for i3 in range(1, i2)[::-1]:
                    if nums[i3] * 2 < left2:
                        break
                    if nums[i3] == last3:
                        continue
                    last3 = nums[i3]
                    left3 = left2 - nums[i3]

                    last4 = None
                    for i4 in range(i3)[::-1]:
                        if nums[i4] == last4:
                            continue
                        last4 = nums[i4]
                        if nums[i4] == left3:
                            sums.append([nums[i1], nums[i2], nums[i3], nums[i4]])

        return sums


s = Solution()
print(s.fourSum([1,0,-1,0,-2,2], 0))
