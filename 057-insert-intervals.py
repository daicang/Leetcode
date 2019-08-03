class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        def merge(i):
            j = i + 1
            while j < len(intervals):
                if intervals[j][0] <= intervals[i][1]:
                    intervals[i][1] = max(intervals[i][1], intervals[j][1])
                    del intervals[j]
                else:
                    break

        for i, val in enumerate(intervals):
            if newInterval[0] <= val[0]:
                intervals.insert(i, newInterval)
                merge(i)
                break
            if newInterval[0] <= val[1]:
                intervals[i][1] = max(intervals[i][1], newInterval[1])
                merge(i)
                break

        else:
            intervals.append(newInterval)

        return intervals





