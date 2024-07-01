class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        min_avg = nums[-1]
        i, j = 0, len(nums)-1
        while i < j:
            min_avg = min(min_avg, (nums[i]+nums[j])/2)
            i += 1
            j -= 1
        return min_avg
