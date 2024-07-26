class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key=lambda x: x[0])

        i = 0
        for j in range(len(intervals)):
            if intervals[j][0] <= intervals[i][1]:
                # merge with i
                intervals[i][1] = max(intervals[i][1], intervals[j][1])
            else:
                merged.append(intervals[i])
                i = j
        # append last one
        merged.append(intervals[i])

        return merged