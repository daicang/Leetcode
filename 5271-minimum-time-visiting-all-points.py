class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        total_time = 0

        for i, point in enumerate(points):
            if i > 0:
                last = points[i-1]

                dx = abs(point[0] - last[0])
                dy = abs(point[1] - last[1])

                total_time += max(dx, dy)

        return total_time


