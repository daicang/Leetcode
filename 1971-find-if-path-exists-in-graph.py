
from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        path = {}
        for edge in edges:
            p1, p2 = edge
            if path.get(p1) is None:
                path[p1] = set()
            path[p1].add(p2)

            if path.get(p2) is None:
                path[p2] = set()
            path[p2].add(p1)

        q = deque()
        q.append(source)
        visited = set()

        while q:
            node = q.popleft()
            if node == destination:
                return True
            visited.add(node)
            relatives = path.get(node)
            if relatives:
                for n in relatives:
                    if n in visited:
                        continue
                    q.append(n)

        return False