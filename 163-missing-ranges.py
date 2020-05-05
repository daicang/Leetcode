from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ranges = []
        nums = [n for n in nums if n >= lower and n <= upper]
        if len(nums) == 0:
            if lower == upper:
                return [str(lower)]
            return ['%s->%s' % (lower, upper)]

        if lower == upper:
            return []
        first_element = nums[0]
        last_element = nums[0]
        for i, n in enumerate(nums):
            if i > 0 and n == last_element + 2:
                ranges.append(str(last_element+1))
            if i > 0 and n > last_element + 2:
                ranges.append('%s->%s' % (last_element+1, n-1))
            last_element = n

        if first_element == lower + 1:
            ranges.insert(0, str(lower))
        elif first_element > lower + 1:
            ranges.insert(0, '%s->%s' % (lower, first_element-1))

        if last_element == upper - 1:
            ranges.append(str(upper))
        elif last_element < upper - 1:
            ranges.append('%s->%s' % (last_element+1, upper))

        return ranges

s = Solution()

data = [
    [[0, 1, 3, 50, 75], 0, 99],
    [[-1], -1, -1],
    [[-1], -2, -1]
]

for d in data:
    print(s.findMissingRanges(*d))

