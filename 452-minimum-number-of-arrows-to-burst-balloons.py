class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 1
        points.sort(key=lambda x: x[1])

        end = points[0][1]
        for x_start, x_end in points:
            if x_start > end:
                end = x_end
                count += 1
        return count
