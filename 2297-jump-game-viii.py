
class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        # costs(i) = min(costs(i)+costs(i-1), costs(i)+costs(first nums[j] >= nums[i] if nums[i-1] < nums[i]))
        #                                                    first nums[j] < nums[i] if nums[i-1] >= nums[i]))
        # length ~= 10^5, single pass only
        # monotonic stack
