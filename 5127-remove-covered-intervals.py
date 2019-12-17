class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        def compare(i1, i2):
            if i1[0] < i2[0]:
                return -1
            elif i1[0] > i2[0]:
                return 1
            else:
                if i1[1] < i2[1]:
                    return 1
                elif i1[1] > i2[1]:
                    return -1
                return 0

        s_intervals = sorted(intervals, cmp=compare)
        counter = 0
        last_interval = None

        for i, interval in enumerate(s_intervals):
            if i == 0:
                last_interval = interval
                counter += 1
                continue

            if interval[1] <= last_interval[1]:
                continue

            counter += 1
            last_interval = interval

        return counter

s = Solution()

data = [
    [[1,4],[3,6],[2,8]],
    # 3
    [[66672,75156],[59890,65654],[92950,95965],[9103,31953],[54869,69855],[33272,92693],[52631,65356],[43332,89722],[4218,57729],[20993,92876]],
]

for d in data:
    print s.removeCoveredIntervals(d)
