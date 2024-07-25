class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        non_overlaps = 1
        end = intervals[0][1]
        for x_begin, x_end in intervals:
            if x_begin >= end:
                end = x_end
                non_overlaps += 1
        return len(intervals) - non_overlaps
