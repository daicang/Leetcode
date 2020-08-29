from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key

        def compare_i(n1, n2):
            return compare_s(str(n1), str(n2))

        def compare_s(s1, s2):
            # return -1 if s1 < s2
            if s1 == s2:
                return 0
            if s1.startswith(s2):
                return compare_s(s1[len(s2):], s2)
            if s2.startswith(s1):
                return compare_s(s1, s2[len(s1):])
            if s1 < s2:
                return -1
            return 1

        sorted_nums = sorted(nums, key=cmp_to_key(compare_i), reverse=True)
        all_zero = True
        for i in sorted_nums:
            if i != 0:
                all_zero = False
                break
        if all_zero:
            return '0'

        return ''.join([str(i) for i in sorted_nums])


s = Solution()

inputs = [
    [3,30,34,5,9],
    [3,43,48,94,85,33,64,32,63,66],
]

for i in inputs:
    print(s.largestNumber(i))
