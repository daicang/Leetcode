from typing import List
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # TLE
        # Time: O(n^2)
        # Space: O(n)
        edges = set()
        skyline = []
        for left, right, h in buildings:
            edges.add(left)
            edges.add(right)

        edges = sorted(list(edges))

        for edge in edges:
            h = 0
            for left, right, height in buildings:
                if left <= edge < right:
                    h = max(h, height)
            if skyline and h == skyline[-1][1]:
                continue
            skyline.append([edge, h])

        return skyline

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Single heapq
        # Time: O(nlog(n))
        # Space: O(n)
        edges = []
        for i, build in enumerate(buildings):
            edges.append([build[0], i])
            edges.append([build[1], i])

        edges.sort()

        q = []
        skyline = []
        i = 0

        while i < len(edges):
            x = edges[i][0]

            # same x for multiple buildings
            while i < len(edges) and edges[i][0] == x:
                build_i = edges[i][1]
                left, right, height = buildings[build_i]
                if left == x:
                    # entering this building
                    heapq.heappush(q, [-height, right])
                i += 1

            while q and q[0][1] <= x:
                # exiting the building
                heapq.heappop(q)


            h = -q[0][0] if q else 0

            if not skyline or h != skyline[-1][1]:
                skyline.append([x, h])

        return skyline

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # print('input: ', buildings)
        # l, r, h
        skyline = []
        curr_height = 0
        curr_idx = 0
        downsteps = []

        for i, building in enumerate(buildings):
            li, ri, height = building

            if height > curr_height:
                curr_height = height
                # print('up at %s to %s' % (li, height))
                skyline.append([li, curr_height])

            curr_idx = li
            # We want to pop max height first

            heapq.heappush(downsteps, [-height, ri])

            next_li = None
            if i < len(buildings)-1:
                next_li, _, _ = buildings[i+1]

            while downsteps:
                down_h, down_idx = downsteps[0]
                down_h *= -1
                # print('check down at %s from %s' % (down_idx, down_h))
                if down_idx <= curr_idx:
                    continue

                if next_li and down_idx > next_li:
                    break

                # Going down at down_idx, find the next height
                heapq.heappop(downsteps)
                curr_idx = down_idx
                down_height = 0
                while downsteps:
                    next_height, next_down_idx = downsteps[0]
                    next_height *= -1
                    if next_down_idx > down_idx:
                        down_height = next_height
                        break
                    heapq.heappop(downsteps)

                curr_height = down_height
                # print('down at %s, from %s to %s' % (down_idx, down_h, down_height))
                skyline.append([down_idx, down_height])

        flat_skyline = []
        for i, val in enumerate(skyline):
            if i > 0:
                last_val = flat_skyline[-1]
                idx, h = val
                last_idx, last_h = last_val
                if idx == last_idx:
                    if h > last_h:
                        flat_skyline[-1][1] = h
                        continue
            flat_skyline.append(val)

        skyline = flat_skyline
        flat_skyline = []
        for i, val in enumerate(skyline):
            if i > 0:
                last_val = flat_skyline[-1]
                idx, h = val
                last_idx, last_h = last_val
                if h == last_h:
                    continue
            flat_skyline.append(val)

        return flat_skyline


s = Solution()

inputs = [
    [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]], # [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    [[0,2,3],[2,5,3]], # [[0, 3], [5, 0]]

]

for i in inputs:
    print(s.getSkyline(i))

# Success
# Details
# Runtime: 154 ms, faster than 79.82% of Python3 online submissions for The Skyline Problem.
# Memory Usage: 18.7 MB, less than 99.36% of Python3 online submissions for The Skyline Problem.
