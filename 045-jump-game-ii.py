class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # TLE
        jumps = [-1] * len(nums)
        jumps[0] = 0

        for i, step in enumerate(nums):
            if i == len(nums)-1:
                break

            if jumps[i] == -1:
                # unreachable
                continue

            jump = jumps[i] + 1
            for j in range(i+1, min(i+step+1, len(nums))):
                if jumps[j] == -1 or jump < jumps[j]:
                    jumps[j] = jump

        return jumps[-1]

    def jump2(self, nums):
        if len(nums) == 1:
            return 0

        jump = 0
        current_bound = next_bound = nums[0]
        i = 1

        while True:
            jump += 1
            if current_bound >= len(nums)-1:
                return jump

            while i <= current_bound:
                next_bound = max(next_bound, i+nums[i])
                i += 1

            if next_bound <= current_bound:
                return -1

            current_bound = next_bound



s = Solution()
inputs = [
    [2,3,1,1,4],
    [2,1],
    [0]
]

for input in inputs:
    print s.jump(input), s.jump2(input)
