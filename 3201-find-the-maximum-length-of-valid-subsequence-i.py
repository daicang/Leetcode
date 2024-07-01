class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # counter[sum_remainder][next_expected_remainder]
        counter = [[0, 0], [0, 0]]
        maxlen = 0

        for n in nums:
            if n % 2 == 0:
                counter[0][0] = counter[0][0] + 1
                counter[1][1] = counter[1][0] + 1
            else:
                counter[0][1] = counter[0][1] + 1
                counter[1][0] = counter[1][1] + 1

        return max(counter[0][0], counter[0][1], counter[1][0], counter[1][1])
