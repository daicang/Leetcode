
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area = abs(ax1 - ax2) * abs(ay1 - ay2) + abs(bx1 - bx2) * abs(by1 - by2)

        x_overlap_start = max(ax1, bx1)
        x_overlap_end = min(ax2, bx2)

        x_overlap = x_overlap_end - x_overlap_start
        if x_overlap <= 0:
            return area

        y_overlap_start = max(ay1, by1)
        y_overlap_end = min(ay2, by2)

        y_overlap = y_overlap_end - y_overlap_start
        if y_overlap <= 0:
            return area

        return area - x_overlap * y_overlap
