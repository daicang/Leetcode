

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        # 2-times bfs traverse
        # time: O(n), space: O(n)
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

        # find farthest node
        _, fnode = bfs(0)
        # bfs from farthest node
        dist, _ = bfs(fnode)

        return dist


    def treeDiameter(self, edges: List[List[int]]) -> int:
        # topological sorting to find centroids
        # time: O(n), space: O(n)
        n = len(edges) + 1
        graph = [set() for i in range(n)]

        for p1, p2, in edges:
            graph[p1].add(p2)
            graph[p2].add(p1)

        leaves = []
        for i, nodes in enumerate(graph):
            if  len(nodes) == 1:
                leaves.append(i)

        r = n
        step = 0
        while r > 2:
            step += 1
            r -= len(leaves)
            new_leaves = []
            for l in leaves:
                for node in graph[l]:
                    graph[node].remove(l)
                    if len(graph[node]) == 1:
                        new_leaves.append(node)
            leaves = new_leaves

        if r == 2:
            return 2 * step + 1
        return 2 * step
