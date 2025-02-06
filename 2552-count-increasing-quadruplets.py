class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        # Count 1-3-2-4 pattern
        n = len(nums)
        count = 0
        count_3 = [0] * n  # 1-3-2 pattern
        for j in range(n):
            count_1 = 0  # 1-2 pattern
            for i in range(j):
                if nums[i] < nums[j]:
                    # up, could be 1-2 or 3-4
                    count_1 += 1
                    count += count_3[i]
                elif nums[i] > nums[j]:
                    # down, could be 3-2
                    count_3[i] += count_1
        return count
