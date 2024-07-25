class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # MST
        # Time: O(v*e)
        # Space: O(v*e)
        graph = []
        for _ in range(n+1):
            graph.append([])

        for v1, v2, cost in connections:
            graph[v1].append((v2, cost))
            graph[v2].append((v1, cost))

        cost = 0
        visited = set()
        h = [[0, 1]]  # [cost, node]

        while h:
            w, i = heapq.heappop(h)
            if i in visited:
                continue
            visited.add(i)
            cost += w
            for j, c in graph[i]:
                if j not in visited:
                    heapq.heappush(h, (c, j))

        if len(visited) < n:
            return -1
        return cost
