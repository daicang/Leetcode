import math

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:

        def build_graph(edges):
            n = len(edges) + 1
            graph = []
            for _ in range(n):
                graph.append(set())
            for p1, p2 in edges:
                graph[p1].add(p2)
                graph[p2].add(p1)
            return graph

        def get_diameter(graph):
            # topological sorting
            print(len(graph))
            if len(graph) in (0, 1):
                return 0
            if len(graph) == 2:
                return 1

            leaves = []
            for i, nodes in enumerate(graph):
                if len(nodes) == 1:
                    leaves.append(i)

            layers = 0
            remaining = len(graph)
            while remaining > 2:
                remaining -= len(leaves)
                layers += 1
                new_leaves = []
                for l in leaves:
                    for node in graph[l]:
                        graph[node].remove(l)
                        if len(graph[node]) <= 1:
                            new_leaves.append(node)
                leaves = new_leaves

            if remaining == 2:
                return 2 * layers + 1
            return 2 * layers

        g1 = build_graph(edges1)
        g2 = build_graph(edges2)

        d1 = get_diameter(g1)
        d2 = get_diameter(g2)
        # max height = meth.ceil(diameter)
        h1 = math.ceil(d1 / 2)
        h2 = math.ceil(d2 / 2)

        return max(h1+h2+1, d1, d2)
