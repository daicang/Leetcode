
from collections import deque

class Solution:
    def canMeasureWater_math(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        def gcd(a, b):
            while a > 0 and b > 0:
                if a > b:
                    a, b = a-b, b
                elif a < b:
                    a, b = a, b-a
                else:
                    return a
            if a == 0:
                return b
            return a
        if targetCapacity > jug1Capacity+jug2Capacity:
            return False
        return targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0


    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        visited = set()
        q = deque()
        q.append((0, 0))

        while q:
            j1, j2 = q.popleft()
            if (j1, j2) in visited:
                continue
            visited.add((j1, j2))
            if j1 == targetCapacity or j2 == targetCapacity or j1+j2 == targetCapacity:
                return True
            # Fill
            if j1 < jug1Capacity:
                q.append((jug1Capacity, j2))
            if j2 < jug2Capacity:
                q.append((j1, jug2Capacity))
            # Empty
            if j1 > 0:
                q.append((0, j2))
            if j2 > 0:
                q.append((j1, 0))
            # Pour
            # j1 -> j2
            if j1 > 0 and j2 < jug2Capacity:
                water = min(j1, jug2Capacity-j2)
                q.append((j1-water, j2+water))
            # j2 -> j1
            if j2 > 0 and j1 < jug1Capacity:
                water = min(j2, jug1Capacity-j1)
                q.append((j1+water, j2-water))

        return False
