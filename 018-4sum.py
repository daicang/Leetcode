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

        for l1 in range(len(nums)-3):
            if l1 > 0 and nums[l1] == nums[l1-1]:
                continue

            if nums[l1] * 4 > target:
                break

            for r1 in range(l1+3, len(nums))[::-1]:
                if r1 < len(nums)-1 and nums[r1] == nums[r1+1]:
                    continue

                if nums[l1] + 3 * nums[r1] < target:
                    break

                new_target = target - nums[l1] - nums[r1]
                l2 = l1 + 1
                r2 = r1 - 1
                while l2 < r2:
                    s = nums[l2] + nums[r2]
                    if s == new_target:
                        sums.append([nums[l1], nums[l2], nums[r2], nums[r1]])
                        last_l2 = nums[l2]
                        last_r2 = nums[r2]
                        l2 += 1
                        while l2 < r2 and nums[l2] == last_l2:
                            l2 += 1
                        r2 -= 1
                        while l2 < r2 and nums[r2] == last_r2:
                            r2 -= 1
                    elif s < new_target:
                        l2 += 1
                    else:
                        r2 -= 1

        return sums


s = Solution()
print(s.fourSum([1,0,-1,0,-2,2], 0))
