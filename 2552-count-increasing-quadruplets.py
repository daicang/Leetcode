class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        arr = [0] * n
        for j in range(n):
            prev_small = 0
            for i in range(j):
                if nums[i] < nums[j]:
                    prev_small += 1
                    count += arr[i]
                elif nums[i] > nums[j]:
                    arr[i] += prev_small
        return count
