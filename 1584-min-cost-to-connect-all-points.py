class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n

        h = [(0, 0)]
        mst_cost = 0
        edges = 0

        while edges < n:
            weight, node = heapq.heappop(h)
            if visited[node]:
                continue

            visited[node] = True
            mst_cost += weight
            edges += 1

            for next_node in range(n):
                if not visited[next_node]:
                    c0, c1 = points[node]
                    cn0, cn1 = points[next_node]
                    weight = abs(c0 - cn0) + abs(c1 - cn1)
                    heapq.heappush(h, (weight, next_node))

        return mst_cost
