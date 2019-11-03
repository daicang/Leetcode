class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def is_odd(val):
            return val % 2 == 1

        odd_positions = []
        for i, val in enumerate(nums):
            if is_odd(val):
                odd_positions.append(i)

        if len(odd_positions) < k:
            return 0

        count = 0
        for i, first_odd_position in enumerate(odd_positions):
            last_odd_i = i + k - 1
            if last_odd_i >= len(odd_positions):
                break

            if i == 0:
                even_count_before_first_odd = first_odd_position
            else:
                even_count_before_first_odd = first_odd_position - odd_positions[i-1] - 1

            if last_odd_i == len(odd_positions)-1:
                even_count_after_last_odd = len(nums) - odd_positions[last_odd_i] - 1
            else:
                even_count_after_last_odd = odd_positions[last_odd_i+1] - odd_positions[last_odd_i] - 1

            count += (even_count_before_first_odd+1) * (even_count_after_last_odd+1)

        return count

s = Solution()

inputs = [
    [[1,1,2,1,1], 3],  #3
    [[2,4,6], 1], # 0
    [[2,2,2,1,2,2,1,2,2,2], 2],  # 16
]

for i in inputs:
    print s.numberOfSubarrays(*i)
