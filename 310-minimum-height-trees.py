from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # topological sorting
        # space: O(n), time: O(n)
        if n <= 2:
            return list(range(n))

        graph = defaultdict(set)

        for p1, p2 in edges:
            graph[p1].add(p2)
            graph[p2].add(p1)

        leaves = []
        for i, nodes in graph.items():
            if len(nodes) == 1:
                leaves.append(i)

        while leaves:
            if len(graph) <= 2:
                # last 2 nodes are centroids
                return graph.keys()
            next_leaves = []
            for leaf in leaves:
                for node in graph[leaf]:
                    graph[node].remove(leaf)
                    if len(graph[node]) == 1:
                        next_leaves.append(node)
                del graph[leaf]

            leaves = next_leaves
