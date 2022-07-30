

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []

        start = 0
        end = 0
        i = 0
        while i < len(nums):
            n = nums[i]
            if i == 0:
                start = n
                end = n
            else:
                if n == end + 1:
                    # continue last range
                    end = n
                else:
                    # save last range and start a new range
                    if start == end:
                        ranges.append(str(start))
                    else:
                        ranges.append('%s->%s' % (start, end))
                    start = end = n

            if i == len(nums)-1:
                # last element
                if start == end:
                    ranges.append(str(start))
                else:
                    ranges.append('%s->%s' % (start, end))

            i += 1


        return ranges
