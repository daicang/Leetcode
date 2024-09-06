class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        count = 0
        graph = []
        for _ in range(n):
            graph.append([])

        for src, dst in connections:
            graph[src].append((dst, src))
            graph[dst].append((src, src))

        visited = [False] * n
        visited[0] = True

        q = deque(graph[0])

        while q:
            node, src = q.popleft()
            if visited[node]:
                continue
            visited[node] = True
            if node != src:
                count += 1
            for n, src in graph[node]:
                if not visited[n]:
                    q.append((n, src))

        return count