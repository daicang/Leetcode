class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        right_q = []
        highest_right = 0
        for idx, h in reversed(list(enumerate(height))):
            if h > highest_right:
                highest_right = h
                right_q.append((idx, h))

        left_q = []
        highest_left = 0
        for idx, h in enumerate(height):
            if h > highest_left:
                highest_left = h
                left_q.append((idx, h))

        max_water = 0
        right_q_start_idx = 0

        for start_idx, start_h in left_q:
            if start_idx >= right_q[right_q_start_idx][0]:
                break

            rq_idx = right_q_start_idx
            for end_idx, end_h in right_q[right_q_start_idx:]:
                width = end_idx - start_idx
                water = width * min(start_h, end_h)

                if water > max_water:
                    max_water = water
                    right_q_start_idx = rq_idx

                rq_idx += 1

        return max_water

s = Solution()


import json
from datetime import datetime

def timeit(func):
    def timed(*args, **kwargs):
        start = datetime.now()
        ret = func(*args, **kwargs)
        print('Time used: %ss' % (datetime.now() - start).total_seconds())
        return ret
    return timed

with open('011-input') as fd:
    l = json.load(fd)

# assert s.maxArea([3, 2, 1, 3]) == 9
# assert s.maxArea([1, 1]) == 1
# assert s.maxArea([1, 2, 4, 3]) == 4

print [5,2,12,1,5,3,4,11,9,4]
assert s.maxArea([5,2,12,1,5,3,4,11,9,4]) == 55

print(timeit(s.maxArea)(l))

