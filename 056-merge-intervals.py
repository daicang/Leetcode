class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key=lambda x: x[0])

        lasti = 0
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[lasti][1]:
                intervals[lasti][1] = max(intervals[i][1], intervals[lasti][1])
                del intervals[i]
            else:
                i += 1
                lasti += 1

        return intervals
