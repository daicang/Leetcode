from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key=lambda x: x[0])

        for i, val in enumerate(intervals):
            print(intervals)
            if i > 0:
                start = val[0]
                last_end = intervals[i-1][1]
                if start < last_end:
                    return False

        return True

s = Solution()

inputs = [
    [[7,10],[2,4]],
]

for i in inputs:
    print(s.canAttendMeetings(i))
