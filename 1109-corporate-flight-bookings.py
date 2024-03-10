
from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diffs = [0] * (n+1)
        for begin, end, incr in bookings:
            diffs[begin-1] += incr
            diffs[end] -= incr

        for i, val in enumerate(diffs):
            if i > 0:
                diffs[i] = diffs[i-1] + val

        return diffs[:n]
