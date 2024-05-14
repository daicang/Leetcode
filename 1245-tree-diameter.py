

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = [set() for i in range(len(edges)+1)]
        for edge in edges:
            u, v = edge
            graph[u].add(v)
            graph[v].add(u)

        def bfs(start):
            visited = [False] * len(graph)
            visited[start] = True
            q = [start]
            distance = -1
            last_node = start

            while q:
                next_q = []
                for node in q:
                    for n in graph[node]:
                        if not visited[n]:
                            visited[n] = True
                            next_q.append(n)
                            last_node = n

                q = next_q
                distance += 1

            return distance, last_node

        dist, fnode = bfs(0)
        dist, _ = bfs(fnode)

        return dist